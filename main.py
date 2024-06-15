from googletrans import Translator
from summarizer import Summarizer
import streamlit as st


def translate_to_english(text):
    translator = Translator()
    translation = translator.translate(text, src='ta', dest='en')
    return translation.text

def summarize_text(text):
    summarizer = Summarizer()
    summary = summarizer(text)
    return summary


def translate_to_tamil(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='ta')
    return translation.text

st.header("Tamil Text Summarizer 📃")


tamil_text = st.text_area("Enter Tamil Text")



if st.button("Submit"):
    english_text = translate_to_english(tamil_text)
    summary_text = summarize_text(english_text)
    translated_summary = translate_to_tamil(summary_text)
    if translated_summary:
        st.subheader("Summarized Text")
        st.write(translated_summary)

