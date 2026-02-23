import streamlit as st
import time
from newspaper import Article
from openai import OpenAI

st.set_page_config(page_title="Site Summarizer", page_icon="📰", layout="wide")

if "library" not in st.session_state:
    st.session_state.library = []

menu = st.sidebar.selectbox("Navigation", ["Home", "My Library"])

if menu == "My Library":
    st.title("📚 Your Saved Summaries")
    if not st.session_state.library:
        st.write("Your library is empty. Save summaries from the Home page!")
    else:
        cols = st.columns(3)
        for i, item in enumerate(st.session_state.library):
            with cols[i % 3]:
                with  st.container(boreder=True):
                    st.subheader(item["title"])
                    st.write(item["summary"])
                    st.markdown(f"[Read Original Article]({item['url']})")


else:
    st.title("🚀 SiteSnapshot AI")
    st.markdown("""
    **Welcome to the future of reading.** Paste any article link below. Our AI will crawl the content, extract the core message, 
    and save it to your personal library as a digital card.
    """)

    url = st.text_input("🔗 Paste your URL link here:", placeholder="https://example.com/cool-article")

    if url:
        # Step 1: Estimated Time Calculation (Mock logic)
        st.info("⏱️ **Estimated time:** 5-8 seconds (Extracting text & AI processing)")
        
        if st.button("Generate Summary"):
            with st.spinner("Processing..."):
                try:
                    # Step 2: Extracting Text
                    article = Article(url)
                    article.download()
                    article.parse()
                    
                    # Step 3: AI Call (Replace 'your-key' with your actual variable)
                    # For this example, we'll simulate the AI text
                    time.sleep(2) # Making it feel real
                    title = article.title if article.title else "Summarized Article"
                    summary_text = "This is where the AI generated summary would appear..."
                    
                    # Step 4: Add to Library
                    new_entry = {
                        "title": title,
                        "summary": summary_text,
                        "url": url
                    }
                    st.session_state.library.append(new_entry)
                    
                    st.success(f"✅ Finished! '{title}' has been added to your Library.")
                    st.balloons()
                    
                except Exception as e:
                    st.error(f"Error: {e}")