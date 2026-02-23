import streamlit as st
import sqlite3
import google.generativeai as genai
from newspaper import Article

# --- DATABASE SETUP ---
conn = sqlite3.connect('summaries.db', check_same_thread=False)
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS library (id INTEGER PRIMARY KEY, title TEXT, summary TEXT, url TEXT)')
conn.commit()

# --- GEMINI SETUP ---
# You can hardcode your key here for local use, 
# or use st.sidebar.text_input for sharing.
API_KEY = "YOUR_GEMINI_API_KEY_HERE" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- APP UI ---
st.set_page_config(page_title="SiteSnapshot Gemini", layout="wide")

tab1, tab2 = st.tabs(["🚀 Home", "📚 Library"])

with tab1:
    st.title("🚀 SiteSnapshot AI (Gemini Edition)")
    url = st.text_input("🔗 Paste URL:")
    
    if st.button("Summarize & Save"):
        with st.spinner("Gemini is reading the site..."):
            try:
                # 1. Scrape
                article = Article(url)
                article.download()
                article.parse()
                
                # 2. Gemini AI Call
                prompt = f"Summarize this article in 3 bullet points with a catchy title. Format it clearly. Content: {article.text[:10000]}"
                response = model.generate_content(prompt)
                summary = response.text
                title = article.title if article.title else "New Entry"
                
                # 3. Save to DB
                c.execute('INSERT INTO library (title, summary, url) VALUES (?, ?, ?)', (title, summary, url))
                conn.commit()
                st.success("Done!")
                st.balloons()
            except Exception as e:
                st.error(f"Error: {e}")

with tab2:
    st.title("📚 Saved Summaries")
    c.execute('SELECT * FROM library ORDER BY id DESC')
    for item in c.fetchall():
        with st.container(border=True):
            st.subheader(item[1])
            st.markdown(item[2])
            st.caption(f"Link: {item[3]}")