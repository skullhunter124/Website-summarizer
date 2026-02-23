import streamlit as st
import sqlite3
import time
from newspaper import Article
from openai import OpenAI

# --- DATABASE SETUP ---
conn = sqlite3.connect('summaries.db', check_same_thread=False)
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS library (id INTEGER PRIMARY KEY, title TEXT, summary TEXT, url TEXT)')
conn.commit()

# --- APP UI CONFIG ---
st.set_page_config(page_title="SiteSnapshot", layout="wide", page_icon="🚀")

# Custom CSS for a cleaner look
st.markdown("""
    <style>
    .stMain { background-color: #f8f9fa; }
    .st-emotion-cache-1r6slb0 { border-radius: 15px; border: 1px solid #e0e0e0; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# --- TOP NAVIGATION ---
# Instead of sidebar, we use tabs for a cleaner "website" feel
tab1, tab2 = st.tabs(["🚀 Home / New Summary", "📚 Saved Library"])

with tab1:
    st.title("SiteSnapshot AI")
    st.caption("Turn long websites into digestible smart cards instantly.")
    
    # API Key in the sidebar keeps the main screen clean
    api_key = st.sidebar.text_input("OpenAI API Key", type="password", help="Get your key at platform.openai.com")
    
    # Main Input Area
    with st.container(border=True):
        url = st.text_input("🔗 Paste the website link you want to summarize:", placeholder="https://example.com/article")
        
        if url:
            st.info("⏱️ **Estimated time:** ~6 seconds")
            if st.button("Generate Summary ✨", use_container_width=True):
                if not api_key:
                    st.error("Please enter your OpenAI API Key in the sidebar first!")
                else:
                    with st.spinner("AI is reading and thinking..."):
                        try:
                            article = Article(url)
                            article.download()
                            article.parse()
                            
                            client = OpenAI(api_key=api_key)
                            response = client.chat.completions.create(
                                model="gpt-4o-mini",
                                messages=[{"role": "user", "content": f"Summarize this in 3 bullet points with a catchy title: {article.text[:3000]}"}]
                            )
                            summary = response.choices[0].message.content
                            title = article.title if article.title else "Summarized Page"
                            
                            # Save to Database
                            c.execute('INSERT INTO library (title, summary, url) VALUES (?, ?, ?)', (title, summary, url))
                            conn.commit()
                            
                            st.success("Analysis Complete! Find your card in the 'Saved Library' tab.")
                            st.balloons()
                        except Exception as e:
                            st.error(f"Something went wrong: {e}")

with tab2:
    st.title("Your Digital Library")
    
    # Fetch from Database
    c.execute('SELECT * FROM library ORDER BY id DESC')
    data = c.fetchall()
    
    if not data:
        st.info("No summaries yet! Go to the Home tab to create one.")
    else:
        # Create a 3-column grid for the cards
        cols = st.columns(3)
        for i, item in enumerate(data):
            with cols[i % 3]:
                # FIXED TYPO HERE: border=True
                with st.container(border=True):
                    st.markdown(f"### {item[1]}") # Title
                    st.write(item[2])            # Summary
                    st.divider()
                    st.link_button("View Original", item[3], use_container_width=True)
                    if st.button(f"Delete", key=f"del_{item[0]}", use_container_width=True):
                        c.execute('DELETE FROM library WHERE id=?', (item[0],))
                        conn.commit()
                        st.rerun()