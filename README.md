# SmartSummaryApp
# 🧠 SmartSummaryApp – AI Article Summarizer

This is a Streamlit-based app that summarizes long articles into short, clear paragraphs using an offline HuggingFace model (`facebook/bart-large-cnn`).  
It's lightweight, private, and works without API keys.

## 🔍 Features

- Paste any article or long text
- Get a one-paragraph intelligent summary
- Uses offline NLP models (no need for OpenAI)

## 🖥️ Screenshot

![screenshot](screenshots/screenshot1.png)

## 🚀 How to Run

```bash
pip install -r requirements.txt
streamlit run summarizer_app.py
