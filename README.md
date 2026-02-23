# 🚀 Website-summarizer

**Website-summarizer** is a high-performance web utility designed to transform complex, long-form articles into concise, actionable 3-point AI summaries. Leveraging Google’s Gemini 2.5 Flash, it allows users to instantly extract core insights and curate a persistent local library of content.

## 🛠️ Local Installation & Setup

Follow these steps to configure and deploy the application on your local machine.

### 1. Prerequisites
* **Python 3.9+**: Ensure Python is installed and configured in your system's PATH.
* **Google Gemini API Key**: 
    1. Log in to [Google AI Studio](https://aistudio.google.com/).
    2. In the bottom-left navigation menu, select **"Get API key"**.
    3. Click the **"Create API key"** button in the top-right corner.
    4. Name your project, generate the key, and **copy** it for the configuration step below.

### 2. Install Dependencies
Initialize your environment by installing the required libraries via your terminal:
```bash
pip install streamlit google-generativeai newspaper3k lxml_html_clean
```
### 3. API Configuration
    1. Open main.py in your prefered code editor.
    2. Navigate to Line 15 and locate the variable:  API_KEY = "YOUR_API_KEY_HERE".
    3. Replace the placeholder string with your unique API key from Google AI Studio.

### 4. Start the Application
Launch the local web server by executing: 
```bash
python -m streamlit run main.py
```
The application will initialize and automatically launch in your default web browser.


**Data Privacy & Storage**
This tool is built with a focus on privacy and local persistence:

    -SQLite Database: All summarized content is stored in a file named summaries.db within your project folder.

    -Local-First: Your saved library remains on your machine. No data is sent to external servers, except for the text sent to the Gemini API for the summarization process.

## Stopping the Application
To safely terminate the local server session:
    1. Return to the terminal windows where the process is running. 
    2. Press CTRL + C on your keyboard to stop the execution



## License
This project is licensed under the MIT License - see the LICENSE file for details