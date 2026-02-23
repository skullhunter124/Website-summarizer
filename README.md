🚀 Website-summarizer
Website-summarizer is a high-performance web utility that transforms complex, long-form articles into concise, 3-point AI summaries. By integrating Google's Gemini 1.5 Flash, it allows users to extract core insights instantly and curate a persistent local library of summarized content.

🛠️ Local Installation & Setup
Follow these steps to configure and execute the application on your local machine.

1. Prerequisites
Python 3.9+: Ensure Python is installed and configured in your system environment.

Google Gemini API Key:

Log in to Google AI Studio.

Select "Get API key" in the bottom-left navigation menu.

Click "Create API key" in the top-right corner.

Generate and copy your unique API key.

2. Install Dependencies
Initialize your environment by installing the necessary libraries via your terminal:

Bash
pip install streamlit google-generativeai newspaper3k lxml_html_clean
3. API Configuration
Open main.py in your code editor.

Navigate to Line 15 and locate the variable: API_KEY = "YOUR_API_KEY_HERE".

Replace the placeholder with your actual API key.

4. Start the Application
Execute the following command to launch the local web server:

Bash
python -m streamlit run main.py
The interface will automatically populate in your default web browser.

🔒 Data Privacy & Storage
Website-summarizer is built with a "local-first" philosophy:

Local Database: All summarized content is stored in a SQLite database file named summaries.db located within your project folder.

Privacy: Your data never leaves your machine, and no external servers (aside from Google's API for the summarization process) have access to your saved library.

⏹️ Stopping the Application
To terminate the local server session:

Return to the terminal window where the app is running.

Press CTRL + C to stop the process.