# Website-summarizer


This is a web tool that turns long, cluttered articles into clean, 3-point AI summaries. It saves your summaries into a local "Library" so you can keep track of everything you've read.

## 🛠️ How to Run Locally

Follow these steps to get the app running on your computer.

### 1. Prerequisites
Make sure you have **Python 3.9+** installed. You will also need a **Gemini API Key** (Free) from [Google AI Studio](https://aistudio.google.com/).
Log in to your google account.
In the bottom left corner you will see Get API key. Then once pressed you will see in the right upper corner a "Create API key" press that, name your key and project. After that copy the API key and paste it in the code.

### 2. Install Dependencies
Open your terminal in the project folder and run:
pip install streamlit google-generativeai newspaper3k lxml_html_clean

### 3. Setup your API KEY
Open main.py and find the line 15, where it says "YOUR API KEY HERE" and replace it with your actual key from Google AI Studio.

### 4. Start the app
python -m streamlit run main.py




## Closing/stoping
Go in the terminal where you opened this and press CTRL + C 
