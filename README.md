# Generative AI with LangChain and Hugging Face

## Overview
This repository contains implementations and examples on Generative AI using **LangChain** and **Hugging Face**. It covers fundamental NLP preprocessing techniques and will expand to include LangChain applications and transformer-based models.

## Repository Structure
```
Generative-AI-with-LangChain-and-Hugging-Face/
│-- 2. NLP feature extraction/
│   ├── 1-Tokenization Example.ipynb
│   ├── 2-Stemming.ipynb
│   ├── 3-Lemmatization.ipynb
│   ├── 4-Stop Words.ipynb
│   ├── 5-Parts of Speech Tagging.ipynb
│   ├── 6-Named Entity Recognition.ipynb
│   ├── 7-One Hot Encoding-P1.ipynb
│   ├── 8-One Hot Encoding-P2.ipynb
│   ├── 9-Bag of Words-P1.ipynb
│   ├── 10 - Bag of Words-P2.ipynb
│   ├── 11 - BOW Implementation using NLTK.ipynb
│   ├── 12 - N-Grams- P1.ipynb
│   ├── 13 - N-gram Implementation using NLTK.ipynb
│-- Datasets/
│   └── spamclassification.csv
```

## Contents
### NLP Preprocessing
#### 1️⃣ Tokenization
- **File:** `1-Tokenization Example.ipynb`
- **Description:** Demonstrates tokenization techniques using libraries like **NLTK, SpaCy, and Hugging Face Tokenizers**.
- **Key Topics:**
  - Word Tokenization
  - Sentence Tokenization
  - Subword Tokenization

#### 2️⃣ Stemming
- **File:** `2-Stemming.ipynb`
- **Description:** Shows how stemming reduces words to their root form using **NLTK’s PorterStemmer and SnowballStemmer**.
- **Key Topics:**
  - Porter Stemmer
  - Snowball Stemmer
  - Differences between Stemming and Lemmatization

#### 3️⃣ Lemmatization
- **File:** `3-Lemmatization.ipynb`
- **Description:** Explores **lemmatization**, which reduces words to their base form while maintaining meaning.
- **Key Topics:**
  - Lemmatization with WordNetLemmatizer
  - Comparison with Stemming
  - Why lemmatization preserves meaning better

#### 4️⃣ Stop Words
- **File:** `4-Stop Words.ipynb`
- **Description:** Removes common words that do not add meaning using NLTK stopword corpus.
- **Key Topics:**
  - Importance of filtering
  - NLTK stopword list
  - Efficiency in modeling
  - Integration with pipelines

#### 5️⃣ POS Tagging
- **File:** `5-Parts of Speech Tagging.ipynb`
- **Description:** Assigns grammatical tags to words for structural analysis.
- **Key Topics:**
  - POS tag types
  - NLTK pos_tag usage
  - Grammar-based preprocessing
  - Use in NER & lemmatization

#### 6️⃣ Named Entity Recognition
- **File:** `6-Named Entity Recognition.ipynb`
- **Description:** Identifies entities like names, organizations, locations using NLTK's chunker.
- **Key Topics:**
  - NER categories
  - Chunk parsing
  - Named entity extraction
  - Use in info retrieval

#### 7️⃣ One-Hot Encoding – Basics
- **File:** `7-One Hot Encoding-P1.ipynb`
- **Description:** Introduces one-hot encoding for word representation with binary vectors.
- **Key Topics:**
  - Vocabulary indexing
  - Binary vectorization
  - Manual examples
  - Role in ML input

#### 8️⃣ One-Hot Encoding – Analysis
- **File:** `8-One Hot Encoding-P2.ipynb`
- **Description:** Discusses pros and cons of one-hot encoding for NLP tasks.
- **Key Topics:**
  - Sparsity issues
  - Lack of semantic context
  - High dimensionality
  - No OOV handling

#### 9️⃣ Bag of Words – Concept
- **File:** `9-Bag of Words-P1.ipynb`
- **Description:** Converts sentences to word frequency vectors using a fixed vocabulary.
- **Key Topics:**
  - Document-term matrix
  - Token counting
  - Stopword filtering
  - Vocabulary creation

#### 🔟 Bag of Words – Evaluation
- **File:** `10 - Bag of Words-P2.ipynb`
- **Description:** Highlights the strengths and weaknesses of BoW for NLP.
- **Key Topics:**
  - No order/context awareness
  - Sparse matrix structure
  - Effective for classification
  - Cannot handle OOV

#### 1️⃣1 BoW from Scratch
- **File:** `11 - BOW Implementation using NLTK.ipynb`
- **Description:** Builds a Bag of Words model using pure Python and NLTK, without scikit-learn.
- **Key Topics:**
  - Text preprocessing & cleaning
  - Tokenization and frequency counting
  - Vector space model basics
  - Foundational understanding of BoW

#### 1️⃣2 N-Grams – Intuition
- **File:** `12 - N-Grams- P1.ipynb`
- **Description:** Demonstrates how bigrams and trigrams capture meaning better than BoW.
- **Key Topics:**
  - N-gram vs BoW comparison
  - Use of `ngram_range`
  - Contextual meaning in sentiment
  - Example-driven explanation

#### 1️⃣3 N-Grams with NLTK
- **File:** `13 - N-gram Implementation using NLTK.ipynb`
- **Description:** Uses NLTK to generate unigrams, bigrams, and trigrams from raw text.
- **Key Topics:**
  - `nltk.ngrams()` usage
  - Manual n-gram generation
  - Tokenization workflow
  - Real text examples

---

## 📝 Medium Article Series

Read the companion blogs on Medium: 📘 [@harsuminder](https://medium.com/@harsuminder)

---
## Installation & Setup
To run the notebooks locally, follow these steps:
```bash
# Clone the repository
git clone https://github.com/Harsuminder/Generative-AI-with-LangChain-and-Hugging-Face.git
cd Generative-AI-with-LangChain-and-Hugging-Face

# Run Jupyter Notebook
jupyter notebook
```

## Future Work
🔹 **LangChain Experiments** (Coming Soon)  
🔹 **Hugging Face Transformer Models** (Coming Soon)  
🔹 **Fine-Tuning LLMs for Applications** (Coming Soon)  

## Author
**Harsuminder Kaur Gill**  
🔗 [GitHub](https://github.com/Harsuminder) | 🔗 [LinkedIn](https://www.linkedin.com/in/harsuminder/) | 🔗 [Medium](https://medium.com/@harsuminder)

## Contributions
Feel free to fork this repo, open issues, or submit pull requests to improve it!
