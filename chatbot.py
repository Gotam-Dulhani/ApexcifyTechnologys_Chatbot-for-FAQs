import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import gradio as gr
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
        print(f"Error: {filepath} not found.")
        return [], []
    with open(filepath, 'r', encoding='utf-8') as f:
        faqs = json.load(f)
    questions = [faq['question'] for faq in faqs]
    answers = [faq['answer'] for faq in faqs]
    return questions, answers

# Preprocessing Initialization
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    """Tokenize, lowercase, and lemmatize text."""
    tokens = word_tokenize(text.lower())
    lemmatized = [lemmatizer.lemmatize(word) for word in tokens if word.replace('-', '').isalnum()]
    return " ".join(lemmatized)

# Load and preprocess data
questions, answers = load_faqs()

if not questions:
    print("Warning: No FAQs loaded. The chatbot will not be able to answer questions.")

# Fit TF-IDF Vectorizer
# We fit on the preprocessed questions from our database
processed_questions = [preprocess_text(q) for q in questions]
vectorizer = TfidfVectorizer()
try:
    tfidf_matrix = vectorizer.fit_transform(processed_questions)
except ValueError:
    print("Warning: TF-IDF vectorizer could not fit (likely empty dataset).")
    tfidf_matrix = None

# Similarity Threshold
SIMILARITY_THRESHOLD = 0.2

def get_best_match(user_query, history=None):
    """Process user query and find the most similar FAQ."""
    # History is provided by Gradio ChatInterface, we don't strictly need it for single-turn FAQ matching,
    # but we accept it to be compatible with the interface.
    if not questions or tfidf_matrix is None:
        return "I'm sorry, my knowledge base is currently empty."
        
    processed_query = preprocess_text(user_query)
    query_vector = vectorizer.transform([processed_query])
    
    # Calculate cosine similarity between the user query and all FAQ questions
    similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
    
    # Find the index of the highest similarity score
    best_match_idx = np.argmax(similarities)
    highest_score = similarities[best_match_idx]
    
    # Debug print (optional)
    # print(f"Query: '{user_query}' -> Score: {highest_score:.4f} against '{questions[best_match_idx]}'")
    
    if highest_score >= SIMILARITY_THRESHOLD:
        return answers[best_match_idx]
    else:
        return "I'm sorry, I don't quite understand. Could you try rephrasing your question or asking something else?"

# Gradio Chat Interface setup
def create_ui():
    # ChatInterface automatically handles the chat history and UI layout
    chatbot_ui = gr.ChatInterface(
        fn=get_best_match,
        title="🤖 FAQ Assistant Bot",
        description=(
            "Ask me anything about **Python, AI, Machine Learning, NLP, Data Science, "
            "Web Development, Cybersecurity**, and more! "
            "I use TF-IDF and cosine similarity to find the best answer from over 60 FAQs."
        ),
        examples=[
            "Why use Python for data science?",
            "Which is better: NLTK or SpaCy?",
            "When should I use a virtual environment?",
            "How do I prevent overfitting?",
            "What is a REST API?",
            "Why is cross-validation necessary?",
            "When was the Transformer architecture introduced?",
        ]
    )
    return chatbot_ui

if __name__ == "__main__":
    ui = create_ui()
    # Launch on a local server
    ui.launch(share=False)
