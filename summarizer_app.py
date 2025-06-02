import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Smart Article Summarizer", layout="centered")

@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_summarizer()

st.title("🧠 Smart Article Summarizer (Offline)")
st.subheader("Paste your text below (max ~1000 words):")

user_input = st.text_area("Enter article or long text", height=300)

MAX_CHARS = 3000

if st.button("Summarize"):
    if not user_input.strip():
        st.warning("Please enter some text.")
    elif len(user_input) > MAX_CHARS:
        st.error(f"⚠️ Input too long! Please limit text to {MAX_CHARS} characters.")
    else:
        with st.spinner("Summarizing... please wait"):
            summary = summarizer(
                user_input,
                max_length=250,  # بیشتر از قبل
                min_length=100,  # تضمین یک پاراگراف کامل
                do_sample=False
            )[0]['summary_text']

            st.success("Detailed Summary:")
            st.write(summary)
