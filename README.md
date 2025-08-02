# 📚 Vocab Chat-Bot – NLP-Based Vocabulary Assistant

This is a simple NLP-powered chatbot built with Python and Streamlit. It is designed to help English language learners enrich their vocabulary by providing:

- ✅ Definitions
- ✅ Synonyms
- ✅ Antonyms
- ✅ Example sentences
- ✅ Grammar Checker

---

## 🚀 Features

- 🔎 Search any English word to get its definition, synonyms, antonyms, and examples.
- 💬 User-friendly interface powered by **Streamlit**.
- 📖 Uses **WordNet** via the **NLTK** library for lexical information.
- 🪄 Uses **ibm-granite/granite-3.3-8b-instruct** via the API from **REPLICATE** for grammar checker feature. 

---

## 🛠️ Tech Stack

| Tool      | Description                             |
|-----------|-----------------------------------------|
| Python    | Programming language                    |
| Streamlit | For interactive web interface           |
| NLTK      | Natural Language Toolkit, using WordNet |
| Replicate | API for accessing IBM GRANITE model     |

---

## 📁 Project Structure

- `app.py` - Main Streamlit application
- `utils/` - Utility modules
  - `vocab_helper.py` - Word processing and lookup functions
  - `grammar_checker.py` - Grammar checker funtion using IBM Granite via API from Replicate
  - `main_keyword.py` - Get and extract main keyword, if the input is a sentence
- `venv/` - Virtual environment (protected by .gitignore)
- `requirements.txt` - Project dependencies
- `.gitignore` - Git ignore rules
- `.streamlit` - Configuration
  - `config.toml` - Display configuration
  - `secrets.toml` - API KEY from Replicate (protected by .gitignore)
- `README.md` - Project documentation

---

## 💻 How to Run

1. **Clone the repository**

   Clone the project repository to your local machine:
   ```bash
   git clone https://github.com/coronafloat/vocab-chatbot.git
   cd vocab-chatbot

2. **Create and Activate a Virtual Environment**

    Create and activate your virtual environment (bash terminal):
    ```bash
    python -m venv venv
    # Windows
    source venv/Scripts/activate
    # macOS/Linux
    source venv/bin/activate

3. **Install the Dependencies**

    Install the dependencies:
   ```bash
   pip install -r requirements.txt

4. **API TOKEN Set Up**
    
    Change filename from secrets.toml.example to secrets.toml and fill the value of your API TOKEN

5. **Run the vocab-chatbot**

    How to run Streamlit:
   ```bash
   streamlit run app.py

---

## 🪄 AI Support Explanation

This project strategically leverages the ibm-granite/granite-3.3-8b-instruct AI model for two highly relevant purposes: optimizing code performance and enabling a core application feature. This use of AI provides a tangible impact on the application's development and functionality.

1. **Code Generation and Optimization Using IBM Granite**
    - Faster Performance: The AI-optimized code, which uses generators and itertools.islice, significantly reduces unnecessary iterations in **get_word_info()** function on `vocal_helper.py` file. This results in faster response times when a user searches for a word, improving the overall user experience.
    - Readability and Maintenance: The refactoring makes the code more concise and "Pythonic". As a result, the codebase is easier to read, debug, and maintain in the future.
2. **Using and Implement IBM Granite Model**
    - Access to Advanced Technology: Without leveraging this pre-trained AI model, implementing a reliable grammar checker feature would have been prohibitively complex and resource-intensive, making it impractical for this project.
    - Enhanced Application Value: The use of AI enables a core feature that directly helps users learn English. This drastically increases the application's value and utility, transforming it from a simple dictionary into a more comprehensive learning assistant.