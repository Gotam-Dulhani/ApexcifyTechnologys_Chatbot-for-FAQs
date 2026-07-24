import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import streamlit as st
import os

# Ensure necessary NLTK data is downloaded
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('tokenizers/punkt_tab')
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('punkt')
    nltk.download('punkt_tab')
    nltk.download('wordnet')

# Load FAQs
def load_faqs(filepath='faqs.json'):
    if not os.path.exists(filepath):
        return [], []
    with open(filepath, 'r', encoding='utf-8') as f:
        faqs = json.load(f)
    questions = [faq['question'] for faq in faqs]
    answers = [faq['answer'] for faq in faqs]
    return questions, answers

# Preprocessing Initialization
lemmatizer = WordNetLemmatizer()

ABBREVIATIONS = {
    "ml": "machine learning",
    "ai": "artificial intelligence",
    "nlp": "natural language processing",
    "dev": "development",
    "devs": "developers",
}

def preprocess_text(text):
    text = text.lower().strip().rstrip("?!.,").strip()
    for abbr, full in ABBREVIATIONS.items():
        text = text.replace(abbr, full)
    tokens = word_tokenize(text)
    lemmatized = [lemmatizer.lemmatize(word) for word in tokens if word.replace('-', '').isalnum()]
    return " ".join(lemmatized)

# Load and preprocess data
questions, answers = load_faqs()

processed_questions = [preprocess_text(q) for q in questions]
vectorizer = TfidfVectorizer()
try:
    tfidf_matrix = vectorizer.fit_transform(processed_questions)
except ValueError:
    tfidf_matrix = None

SIMILARITY_THRESHOLD = 0.2

def get_best_match(user_query):
    if not questions or tfidf_matrix is None:
        return "I'm sorry, my knowledge base is currently empty."

    processed_query = preprocess_text(user_query)
    query_vector = vectorizer.transform([processed_query])
    similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
    best_match_idx = np.argmax(similarities)
    highest_score = similarities[best_match_idx]

    if highest_score >= SIMILARITY_THRESHOLD:
        return answers[best_match_idx]
    else:
        return "I'm sorry, I don't quite understand. Could you try rephrasing your question or asking something else?"

# Streamlit UI
st.set_page_config(page_title="FAQ Assistant Bot", page_icon="🤖", layout="centered")
st.title("FAQ Assistant Bot")
st.caption("Ask me anything about Python, AI, ML, NLP, Data Science, Web Dev, Cybersecurity & more!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

examples = [
    "Why use Python for data science?",
    "Which is better: NLTK or SpaCy?",
    "When should I use a virtual environment?",
    "How do I prevent overfitting?",
    "What is a REST API?",
    "Why is cross-validation necessary?",
]

if prompt := st.chat_input("Ask a question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = get_best_match(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
