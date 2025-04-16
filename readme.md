# 🧠 Streamlit Sentiment Analysis App

A minimal and interactive Streamlit frontend for **sentiment analysis**, powered by a [FastAPI backend](https://github.com/96ibman/FastAPI_sentiment_analysis) and Hugging Face's 🤗 `transformers` pipeline.

- ⚡ **Frontend**: Streamlit  
- 🚀 **Backend**: FastAPI (`distilbert-base-uncased-finetuned-sst-2-english`)  
- 📡 **Deployed Backend**: Render  
- 🌐 **Live Demo**: [Available on Hugging Face Spaces](#)

---

## 🔧 Backend Repository (FastAPI)

To see how the API works behind the scenes or run it yourself, check **[my repo](https://github.com/96ibman/FastAPI_sentiment_analysis)**

It uses Hugging Face’s `pipeline("sentiment-analysis")` and exposes a simple `/analyze` POST endpoint.

Example request:

```bash
curl -X POST "https://fastapi-sentiment-analysis.onrender.com/analyze" \
     -H "Content-Type: application/json" \
     -d '{"text": "I love Streamlit!"}'
```

---

## 🚀 Run This Streamlit App Locally

1. **Clone this repository**:

```bash
git clone https://github.com/96ibman/FastAPI_sentimentAnalysis_Streamlit.git
cd FastAPI_sentimentAnalysis_Streamlit
```

2. **Create a virtual environment**:

```bash
python -m venv venv
source venv/bin/activate    # Mac
venv/Scripts/activate       # Win
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Run the app**:

```bash
streamlit run app.py
```

---

## 🌍 Try It Online (Hugging Face Spaces)

> ✨ This app is live and accessible via Hugging Face Spaces

🔗 [**Launch in Hugging Face Spaces**](#)

Just enter any sentence and see if the model thinks it's **positive** or **negative**, along with a confidence score.

> Note: Render might shut down the API so this might not work. Try locally instead in this case.
---

## 📦 Tech Stack

| Layer        | Tool/Library |
|--------------|--------------|
| Frontend UI  | Streamlit    |
| Backend API  | FastAPI      |
| NLP Model    | Hugging Face Transformers |
| Hosting (API) | Render      |
| Hosting (App) | Hugging Face Spaces |
