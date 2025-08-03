import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
import time
from utils.vocal_helper import get_word_info
from utils.grammar_checker import check_grammar
from utils.main_keyword import extract_main_keyword 

nltk.download('wordnet')
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('averaged_perceptron_tagger_eng')

stop_words = set(stopwords.words('english'))

# STYLING CONFIG
st.set_page_config(
    page_title="Vocab-Bot Pro",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="expanded"
)

def load_css():
    st.markdown("""
        <style>
            /* --- Gaya Umum --- */
            .stApp { background-color: #0e1117; }
            .stButton>button {
                border-radius: 10px; border: 2px solid #6c63ff;
                color: #6c63ff; background-color: transparent;
                transition: all 0.2s ease-in-out;
            }
            .stButton>button:hover {
                border-color: #fafafa; color: #fafafa; background-color: #6c63ff;
            }
            .stButton>button:disabled {
                border-color: #444; color: #444; background-color: transparent;
            }
            /* --- Gaya Kartu --- */
            .card {
                background-color: #262730; border-radius: 15px; padding: 25px;
                margin-bottom: 20px; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
                transition: 0.3s;
            }
            .card:hover { box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2); }
            /* --- Gaya Badge untuk Sinonim/Antonim --- */
            .badge-container { display: flex; flex-wrap: wrap; gap: 8px; }
            .badge {
                display: inline-block; padding: 5px 12px; border-radius: 15px;
                font-weight: 500; font-size: 14px;
            }
            .synonym-badge {
                background-color: rgba(4, 170, 109, 0.2); color: #FFF;
                border: 1px solid #04AA6D;
            }
            .antonym-badge {
                background-color: rgba(255, 71, 87, 0.2); color: #FF4757;
                border: 1px solid #FF4757;
            }
        </style>
    """, unsafe_allow_html=True)

load_css()

def run_word_lookup_page():
    st.title("📖 Word Lookup Pro")
    st.write("Get detailed information about any English word.")
    
    input_text = st.text_input("🔍 Ask me about a word...", key="word_lookup_input").strip()
    
    if "current_word" in st.session_state and not input_text:
        del st.session_state.current_word

    word = extract_main_keyword(input_text)

    if word:
        if ("current_word" not in st.session_state or st.session_state.current_word != word.lower()):
            with st.spinner(f"✨ Conjuring up details for '{word}'..."):
                info = get_word_info(word.lower(), max_examples=50)
            
            if info:
                st.session_state.current_word = word.lower()
                st.session_state.info = info
                st.session_state.page = 0
            else:
                st.error(f"🚫 Oops! I couldn't find any information for '{word}'. Please try another.")
                if "current_word" in st.session_state: del st.session_state.current_word
                st.stop()
    else:
        st.info("Start by typing a word or a question in the search box above!")
        st.stop()
    
    info = st.session_state.info
    st.markdown(f"## {st.session_state.current_word.capitalize()}")

    tab1, tab2 = st.tabs(["📝 Definition & Examples", "🔄 Related Words"])

    with tab1:
        st.markdown(f"<div class='card'><p><strong>Definition:</strong><br>{info['definition']}</p></div>", unsafe_allow_html=True)
        
        st.subheader("Example Sentences")
        PAGE_SIZE = 3
        page = st.session_state.get('page', 0)
        start_idx = page * PAGE_SIZE
        end_idx = start_idx + PAGE_SIZE
        
        for i, ex in enumerate(info["examples"][start_idx:end_idx], start=start_idx + 1):
            st.markdown(f"<div class='card' style='padding: 15px;'>{i}. <i>{ex}</i></div>", unsafe_allow_html=True)
        
        total_examples = len(info["examples"])
        max_page = (total_examples - 1) // PAGE_SIZE
        if total_examples > PAGE_SIZE:
            def _nav(step: int):
                st.session_state.page += step
            
            prev_col, page_info, next_col = st.columns([1, 2, 1])
            with prev_col:
                st.button("◀️ Previous", disabled=(page == 0), on_click=_nav, args=(-1,))
            with next_col:
                st.button("Next ▶️", disabled=(page >= max_page), on_click=_nav, args=(1,))
            with page_info:
                st.markdown(f"<div style='text-align: center; margin-top: 10px;'>Page {page + 1} of {max_page + 1}</div>", unsafe_allow_html=True)

    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📗 Synonyms")
            if info['synonyms']:
                badge_html = "".join([f"<span class='badge synonym-badge'>{s}</span>" for s in info['synonyms']])
                st.markdown(f"<div class='card badge-container'>{badge_html}</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='card'><p>—</p></div>", unsafe_allow_html=True)
        with col2:
            st.subheader("📕 Antonyms")
            if info['antonyms']:
                badge_html = "".join([f"<span class='badge antonym-badge'>{a}</span>" for a in info['antonyms']])
                st.markdown(f"<div class='card badge-container'>{badge_html}</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='card'><p>—</p></div>", unsafe_allow_html=True)

def run_vocabulary_improvement_page():
    st.title("🚀 Vocabulary Expansion & Grammar Checker")
    st.write("Elevate your writing by discovering more sophisticated words and ensuring grammatical correctness.")
    
    sentence = st.text_area("Enter your sentence here:", height=150, key="vocab_improve_input", placeholder="e.g., The big dog runs fast...")

    # Checkbox Grammar Checking
    grammar_check = st.checkbox("🧠 Perform Grammar Check")

    if st.button("✨ Analyze & Improve"):
        if not sentence.strip():
            st.warning("Please enter a sentence to analyze.")
            st.stop()

        with st.spinner("Analyzing your sentence..."):
            time.sleep(1)

            # Grammar Check Result
            if grammar_check:
                st.subheader("✅ Grammar-Corrected Sentence:")
                corrected = check_grammar(sentence)
                st.success(corrected)
                sentence = corrected

            # Vocabulary Suggestion
            tokens = word_tokenize(sentence)
            tagged_words = pos_tag(tokens)
            
            improvement_candidates = []
            for word, tag in tagged_words:
                if tag.startswith(('JJ', 'NN', 'VB', 'RB')) and word.lower() not in stop_words and len(word) > 2:
                    improvement_candidates.append(word)
            
            unique_candidates = list(dict.fromkeys(improvement_candidates))

        if not unique_candidates:
            st.success("✅ Your sentence is concise! I couldn't find any common words to improve.")
            st.stop()
        
        st.subheader("🪄 Suggestions for Vocabulary Improvement:")
        found_suggestion = False
        for word in unique_candidates:
            info = get_word_info(word.lower(), max_examples=0)
            if info and info['synonyms']:
                suggestions = [s.replace('_', ' ') for s in info['synonyms'] if s.lower() != word.lower()]
                if suggestions:
                    found_suggestion = True
                    expander = st.expander(f"Alternatives for '{word}'")
                    badge_html = "".join([f"<span class='badge synonym-badge'>{s}</span>" for s in suggestions])
                    expander.markdown(f"<div class='badge-container'>{badge_html}</div>", unsafe_allow_html=True)
        
        if not found_suggestion:
            st.success("✨ Your vocabulary is already quite diverse! I couldn't find any simple alternatives.")

# Sidebar 
st.sidebar.title("✨ Vocab-Bot Pro")
st.sidebar.write("Your personal AI vocabulary assistant.")
menu_selection = st.sidebar.radio(
    "Choose a feature:",
    ("📖 Word Lookup", "🚀 Vocabulary Improver"),
    captions=["Find definitions, examples, etc.", "Get suggestions to enhance your text."]
)

if menu_selection == "📖 Word Lookup":
    run_word_lookup_page()
elif menu_selection == "🚀 Vocabulary Improver":
    run_vocabulary_improvement_page()