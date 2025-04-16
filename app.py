import streamlit as st
import requests

st.set_page_config(page_title="🧠 Sentiment Analysis", layout="centered")
st.title("🧠 Sentiment Analysis via FastAPI")
st.write("Enter some text below and get sentiment prediction using a remote FastAPI service.")

API_URL = "https://fastapi-sentiment-analysis.onrender.com/analyze"

user_input = st.text_area("Enter your text here", height=150)

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Analyzing..."):
            response = requests.post(API_URL, json={"text": user_input})
            if response.status_code == 200:
                result = response.json()
                analysis = result.get("analysis", {})
                label = analysis.get("label", "Unknown")
                score = analysis.get("score", 0.0)
                st.success(f"**Sentiment:** {label} (Confidence: {score:.2%})")
            else:
                st.error(f"Failed to get a valid response from the API. Status code: {response.status_code}")

if st.button("Clear"):
    st.experimental_rerun()
