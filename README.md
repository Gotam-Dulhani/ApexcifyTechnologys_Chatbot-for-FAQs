# FAQ Chatbot using NLP

[![Contributors](https://img.shields.io/github/contributors/Gotam-Dulhani/Chatbot-for-FAQs)](https://github.com/Gotam-Dulhani/Chatbot-for-FAQs/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/Gotam-Dulhani/Chatbot-for-FAQs)](https://github.com/Gotam-Dulhani/Chatbot-for-FAQs/network/members)
[![Stars](https://img.shields.io/github/stars/Gotam-Dulhani/Chatbot-for-FAQs)](https://github.com/Gotam-Dulhani/Chatbot-for-FAQs/stargazers)
[![Issues](https://img.shields.io/github/issues/Gotam-Dulhani/Chatbot-for-FAQs)](https://github.com/Gotam-Dulhani/Chatbot-for-FAQs/issues)
[![License](https://img.shields.io/github/license/Gotam-Dulhani/Chatbot-for-FAQs)](https://github.com/Gotam-Dulhani/Chatbot-for-FAQs/blob/main/LICENSE)

> A **TF-IDF powered FAQ Chatbot** built with Python, NLTK, Scikit-Learn, and Streamlit — matches user queries to the most relevant answer using NLP preprocessing and Cosine Similarity.

---

## Table of Contents

* [About The Project](#about-the-project)
* [Key Features](#key-features)
* [Built With](#built-with)
* [How It Works](#how-it-works)
* [Project Structure](#project-structure)
* [Getting Started](#getting-started)
* [Usage](#usage)
* [Deploy on Streamlit Cloud](#deploy-on-streamlit-cloud)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

---

## About The Project

The **FAQ Chatbot** is an NLP-powered question-answering system that uses **TF-IDF vectorization** and **Cosine Similarity** to find the most mathematically relevant answer to any user query from a custom knowledge base.

It features full NLP preprocessing (tokenization, lemmatization, abbreviation expansion), a smart fallback mechanism for unrecognized questions, and a clean **Streamlit web interface** — all driven by a lightweight `faqs.json` knowledge base that's easy to update.

---

## Key Features

* **Custom Knowledge Base** – Powered entirely by a lightweight `faqs.json` file with 60+ FAQs, easy to extend.
* **NLP Preprocessing** – Lowercasing, tokenization, punctuation filtering, abbreviation expansion, and lemmatization via NLTK.
* **TF-IDF Intent Matching** – Scikit-Learn vectorization to measure term relevance across all FAQ questions.
* **Cosine Similarity Scoring** – Finds the most semantically similar FAQ to any user query.
* **Abbreviation Handling** – Automatically expands shortcuts like "ML" to "machine learning", "AI" to "artificial intelligence", "dev" to "development".
* **Fallback Mechanism** – Gracefully handles unrecognized queries when confidence score drops below `0.2`.
* **Streamlit Web UI** – Clean, modern chat interface with zero frontend code.

---

## Built With

| Technology | Purpose |
|---|---|
| Python 3.8+ | Core language |
| NLTK | Tokenization & lemmatization |
| Scikit-Learn | TF-IDF vectorization & Cosine Similarity |
| Streamlit | Web chat interface |
| JSON | Lightweight FAQ knowledge base |

---

## How It Works

### 1. Data Loading
The bot loads `faqs.json` — a list of `question` and `answer` pairs — and splits them into two parallel lists for processing.

### 2. NLP Preprocessing
Every text input (from the database or user) goes through a pipeline:

| Step | Description |
|---|---|
| **Lowercasing** | `"Python"` and `"python"` become identical |
| **Abbreviation Expansion** | `"ML"` becomes `"machine learning"`, `"dev"` becomes `"development"` |
| **Tokenization** | Text split into individual word tokens via `word_tokenize()` |
| **Filtering** | Punctuation stripped (hyphenated terms like *TF-IDF* preserved) |
| **Lemmatization** | Words reduced to root form — `"running"` → `"run"`, `"libraries"` → `"library"` |

### 3. TF-IDF & Cosine Similarity

```
User Query
    |
    v
Abbreviation Expansion
    |
    v
NLP Preprocessing
    |
    v
TF-IDF Vectorization (against FAQ matrix)
    |
    v
Cosine Similarity Scoring
    |
    v
Score >= 0.2? ---- Yes --> Return Best-Match Answer
    |
    No
    |
    v
Fallback Response
```

* **TF-IDF**: Measures how frequently a term appears in a question vs. how common it is across all questions — highlighting unique, relevant terms.
* **Cosine Similarity**: Measures the angle between the user query vector and each FAQ vector. The FAQ with the highest score wins.

---

## Project Structure

```
Chatbot-for-FAQs/
|
|-- chatbot.py          # Main script -- NLP logic + Streamlit UI
|-- faqs.json           # Knowledge base (questions & answers)
|-- requirements.txt    # Python dependencies
|-- Dockerfile          # Container config for deployment
|-- README.md
```

> To update the bot's knowledge, simply edit `faqs.json` — no code changes needed.

---

## Getting Started

### Prerequisites

* Python 3.8+
* pip

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/Gotam-Dulhani/Chatbot-for-FAQs.git
cd Chatbot-for-FAQs
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

> NLTK corpora (`punkt`, `punkt_tab`, `wordnet`) are downloaded automatically on first run.

---

## Usage

**Start the chatbot server:**

```bash
streamlit run chatbot.py
```

Once initialized, the terminal will display a local URL:

```
Running on local URL: http://localhost:8501
```

Open this link in your browser to interact with the FAQ Assistant via the Streamlit chat interface!

---

## Deploy on Streamlit Cloud

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with your GitHub account
4. Click **New app**
5. Fill in:
   - **Repository**: `Gotam-Dulhani/ApexcifyTechnologys_Chatbot-for-FAQs`
   - **Branch**: `main`
   - **Main file path**: `chatbot.py`
6. Click **Deploy**
7. Your chatbot will be live at `https://<your-username>.streamlit.app`

---

## Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch:

```bash
git checkout -b feature/AmazingFeature
```

3. Commit your changes:

```bash
git commit -m "Add AmazingFeature"
```

4. Push and open a Pull Request:

```bash
git push origin feature/AmazingFeature
```

---

## License

Distributed under the **MIT License**. See `LICENSE` for details.

---

## Contact

**Gotam Dulhani**
GitHub: [https://github.com/Gotam-Dulhani](https://github.com/Gotam-Dulhani)

---

## Acknowledgments

* [NLTK Documentation](https://www.nltk.org/)
* [Scikit-Learn Documentation](https://scikit-learn.org/)
* [Streamlit Documentation](https://docs.streamlit.io/)
* Open Source Community
