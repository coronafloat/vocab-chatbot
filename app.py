import streamlit as st
from utils.vocal_helper import get_word_info

# helper untuk navigasi halaman
def _nav(step: int):
    st.session_state.page += step
    st.session_state.page = max(0, min(st.session_state.page, max_page))

PAGE_SIZE = 3

st.title("Vocab Chat-Bot")
word = st.text_input("Masukkan Kata (EN):").strip()

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
            st.warning("Kata tidak ditemukan di WordNet.")
            st.stop()
else:
    # berhenti merender bila belum ada input
    st.stop() 

info  = st.session_state.info
page  = st.session_state.page
total = len(info["examples"])
max_page = (total - 1) // PAGE_SIZE

# tampilan utama
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