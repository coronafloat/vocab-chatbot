import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from utils.vocal_helper import get_word_info
from nltk.corpus import stopwords
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger_eng')
# nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

# PreProcess Function
def extract_main_keyword(text: str) -> str:
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalnum()]  # buang tanda baca
    tokens_clean = [word for word in tokens if word.lower() not in stop_words]

    if not tokens_clean:
        return None

    tagged = pos_tag(tokens_clean)

    # Prioritas: adjective > noun > verb, dari belakang ke depan (kata terakhir lebih penting)
    priority_tags = ['JJ', 'NN', 'VB']

    for tag_prefix in priority_tags:
        for word, tag in reversed(tagged):
            if tag.startswith(tag_prefix):
                return word.lower()

    return tokens_clean[-1].lower()  # fallback: ambil kata terakhir

# helper untuk navigasi halaman
def _nav(step: int):
    st.session_state.page += step
    st.session_state.page = max(0, min(st.session_state.page, max_page))

PAGE_SIZE = 3

st.title("Vocab Chat-Bot")
input_text = st.text_input("Ask me about a word:").strip()
word = extract_main_keyword(input_text)

# reset state bila kata berubah
if word:
    if ("current_word" not in st.session_state or
        st.session_state.current_word != word.lower()):
        info = get_word_info(word.lower(), max_examples=50)
        if info:
            st.session_state.current_word = word.lower()
            st.session_state.info = info
            st.session_state.page = 0
        else:
            st.warning("Sorry, I can't understand😞")
            st.stop()
else:
    # berhenti merender bila belum ada input
    st.stop() 

info  = st.session_state.info
page  = st.session_state.page
total = len(info["examples"])
max_page = (total - 1) // PAGE_SIZE

# tampilan utama
st.markdown(f"**Word:** {st.session_state.current_word}")
st.markdown(f"**Definition:** {info['definition']}")
st.markdown("**Example Sentences:**")

start, end = page * PAGE_SIZE, (page + 1) * PAGE_SIZE
for idx, ex in enumerate(info["examples"][start:end], start + 1):
    st.markdown(f"{idx}. *{ex}*")

# tombol previous & next
prev_col, next_col = st.columns(2)

with prev_col:
    st.button(
        "◀️ Previous examples",
        disabled=page == 0,
        on_click=lambda: _nav(-1)
    )

with next_col:
    st.button(
        "Next examples ▶️",
        disabled=page >= max_page,
        on_click=lambda: _nav(1)
    )
st.markdown(f"**Synonyms:** {', '.join(info['synonyms']) or '—'}")
st.markdown(f"**Antonyms:** {', '.join(info['antonyms']) or '—'}")