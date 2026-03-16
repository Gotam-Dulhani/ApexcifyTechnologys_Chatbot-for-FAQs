# FAQ Chatbot using NLP

A simple yet effective Frequency-Inverse Document Frequency (TF-IDF) based FAQ Chatbot built with Python, Natural Language Toolkit (NLTK), Scikit-Learn, and Gradio. This project fulfills core NLP requirements by collecting a custom dataset, preprocessing textual queries, matching them based on computed document similarity, and returning the best-matching answer via a modern web interface.

## Table of Contents
- [Features](#features)
- [How It Works](#how-it-works)
    - [1. Data Loading](#1-data-loading)
    - [2. Preprocessing](#2-preprocessing)
    - [3. TF-IDF & Cosine Similarity](#3-tf-idf--cosine-similarity)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Features
- **Custom Knowledge Base**: Driven entirely by a lightweight `faqs.json` database.
- **NLP Preprocessing**: Utilizes NLTK for sentence tokenization and word lemmatization.
- **Intent Matching**: Applies Scikit-Learn's TF-IDF vectorization and Cosine Similarity to find the most mathematically relevant answer to a user's query.
- **Fallback Mechanism**: Gracefully handles unrecognized questions if confidence scores dip below a certain threshold.
- **Gradio UI**: Features a clean web chat interface hosted locally.

## How It Works

### 1. Data Loading
The bot loads a JSON file (`faqs.json`) containing a list of dictionaries with `question` and `answer` key-value pairs. From this, it splits the data into a list of questions and a corresponding list of answers.

### 2. Preprocessing
When text (either from the database or from a user query) enters the system, it undergoes preprocessing using the NLTK library:
- **Lowercasing**: All text is converted to lowercase so that "Python" and "python" are identical.
- **Tokenization**: The text is broken into individual words (tokens) using `word_tokenize()`.
- **Filtering**: Punctuation is stripped. (Hyphenated tech words like *TF-IDF* are preserved).
- **Lemmatization**: Words are reduced to their root dictionary form using `WordNetLemmatizer()` (e.g., "running" becomes "run", "libraries" becomes "library").

### 3. TF-IDF & Cosine Similarity
Once preprocessed, the system relies on Scikit-Learn to match the intent:
- **TF-IDF Vectorization**: The existing FAQ questions are converted into an algorithmic matrix. It measures how frequently a term occurs in a specific question while offsetting it by how often that term occurs across all questions.
- **Cosine Similarity**: When a user inputs a query, it is vectorized against the existing vocabulary matrix. The system then measures the angle (Cosine Similarity) between the user's vector and each FAQ vector. 
- The bot identifies the FAQ with the highest similarity score. If the score is >= `0.2`, it returns the corresponding answer. Otherwise, it triggers the fallback response.

## Installation

1. Make sure you have **Python 3.8+** installed.
2. Clone or navigate to the project repository.
3. Install the necessary dependencies via pip:
```bash
pip install -r requirements.txt
```

*(Note: Essential NLTK corpora like `punkt`, `punkt_tab`, and `wordnet` will be downloaded automatically when running the script for the first time).*

## Usage

Start the chatbot server by running the main Python script:
```bash
python chatbot.py 
```
Once initialized, the terminal will display a local URL (usually `http://127.0.0.1:7860`). Open this link in your web browser to interact with the FAQ Assistant Bot via the Gradio interface!

## Project Structure
- `chatbot.py`: The main execution script containing the backend NLP logic and Gradio frontend configuration.
- `faqs.json`: The database file holding the questions and answers. Modify this directly to update the bot's knowledge.
- `requirements.txt`: The required Python dependencies.
