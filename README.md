# 📚 Vocab Chat-Bot – NLP-Based Vocabulary Assistant

This is a simple NLP-powered chatbot built with Python and Streamlit. It is designed to help English language learners enrich their vocabulary by providing:

- ✅ Definitions
- ✅ Synonyms
- ✅ Antonyms
- ✅ Example sentences (with pagination)

---

## 🚀 Features

- 🔎 Search any English word to get its definition, synonyms, antonyms, and examples.
- 🧠 Interactive navigation of example sentences using **Next** and **Previous** buttons.
- 💬 User-friendly interface powered by **Streamlit**.
- 📖 Uses **WordNet** via the **NLTK** library for lexical information.

---

## 🛠️ Tech Stack

| Tool      | Description                             |
|-----------|-----------------------------------------|
| Python    | Programming language                    |
| Streamlit | For interactive web interface           |
| NLTK      | Natural Language Toolkit, using WordNet |

---

## 📁 Project Structure

- `app.py` - Main Streamlit application
- `utils/` - Utility modules
  - `vocab_helper.py` - Word processing and lookup functions
- `venv/` - Virtual environment (not tracked)
- `requirements.txt` - Project dependencies
- `.gitignore` - Git ignore rules
- `README.md` - Project documentation

---

## 💻 How to Run

1. **Clone the repository**

   Clone the project repository to your local machine:
   ```bash
   git clone https://github.com/coronafloat/vocab-chatbot.git
   cd vocab-chatbot

2. **Create and Activate a Virtual Environment**

    Create and activate your virtual environment:
    ```bash
    python -m venv venv
    # Windows
    venv/Scripts/activate
    # macOS/Linux
    source venv/bin/activate

3. **Install the Dependencies**

    Install the dependencies:
   ```bash
   pip install -r requirements.txt

4. **Run the vocab-chatbot**

    How to run Streamlit:
   ```bash
   streamlit run app.py