import streamlit as st
import sqlite3
import google.generativeai as genai
from newspaper import Article
from newspaper import Config

# --- DATABASE SETUP ---
conn = sqlite3.connect('summaries.db', check_same_thread=False)
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS library (id INTEGER PRIMARY KEY, title TEXT, summary TEXT, url TEXT)')
conn.commit()


# Replace with your actual API key from Google Cloud Console and insert it here. You can create an API key in the Google Cloud Console under the "APIs & Services" section. Make sure to enable the Generative AI API for your project and restrict the key as needed for security.
API_KEY = "YOUR API KEY HERE" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')


st.set_page_config(page_title="SiteSnapshot Gemini", layout="wide", page_icon="🚀")


st.markdown("""
    <style>
    .stMain { background-color: #f9f9f9; }
    .st-emotion-cache-1r6slb0 { border-radius: 12px; padding: 20px; }
    </style>
    """, unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🚀 Home", "📚 Library"])

with tab1:
    st.title("🚀 SiteSnapshot AI")
    st.write("Enter a URL to get an AI-powered summary added to your library.")
    
    url = st.text_input("🔗 Paste URL:", placeholder="https://example.com/article")
    

    if st.button("Summarize & Save", use_container_width=True):
        if not url:
            st.warning("Please paste a URL first!")
        else:
            with st.spinner("Gemini is reading and summarizing..."):
                try:
                    
                    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
                    config = Config()
                    config.browser_user_agent = user_agent
                    config.request_timeout = 15 

                    
                    article = Article(url, config=config)
                    article.download()
                    article.parse()
                    
                    
                    if len(article.text) < 100:
                        st.error("⚠️ The website blocked the scraper or has no readable text. Try a different link.")
                    else:
                        
                        prompt = f"Summarize this article in 3 catchy bullet points with a short title. Content: {article.text[:10000]}"
                        response = model.generate_content(prompt)
                        summary = response.text
                        title = article.title if article.title else "New Entry"
                        
                        
                        c.execute('INSERT INTO library (title, summary, url) VALUES (?, ?, ?)', (title, summary, url))
                        conn.commit()
                        
                        st.success(f"Successfully added '{title}'!")
                        st.balloons()
                except Exception as e:
                    st.error(f"Something went wrong: {e}")

with tab2:
    st.title("📚 Your Saved Summaries")
    
    
    c.execute('SELECT * FROM library ORDER BY id DESC')
    items = c.fetchall()
    
    if not items:
        st.info("Your library is empty. Summarize a website to see it here!")
    else:
        
        cols = st.columns(3)
        for i, item in enumerate(items):
            with cols[i % 3]:
                with st.container(border=True):
                    st.subheader(item[1]) 
                    st.markdown(item[2])  
                    st.caption(f"Source: {item[3]}") 
                    
                    st.divider()
                    
                    
                    btn_col1, btn_col2 = st.columns(2)
                    
                    with btn_col1:
                        
                        if st.button("📋 Copy", key=f"copy_{item[0]}", use_container_width=True):
                            st.toast("Highlight text above to copy!")
                    
                    with btn_col2:
                        
                        if st.button("🗑️ Delete", key=f"del_{item[0]}", use_container_width=True):
                            c.execute('DELETE FROM library WHERE id=?', (item[0],))
                            conn.commit()
                            st.rerun()
                            
                    st.link_button("🌐 Open Website", item[3], use_container_width=True)