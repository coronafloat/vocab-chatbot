import streamlit as st
from utils.vocal_helper import get_word_info  

st.title("Vocab Chat-Bot")
word = st.text_input("Masukkan kata (EN):")

if word:
    info = get_word_info(word.lower(), max_examples=3)   # ambil hingga 3 contoh
    if info:
        st.markdown(f"**Defnition:** {info['definition']}")

        st.markdown("**Example of Sentences:**")
        for idx, ex in enumerate(info["examples"], 1):
            st.markdown(f"{idx}. *{ex}*")

        st.markdown(f"**Synonym:** {', '.join(info['synonyms']) or '—'}")
        st.markdown(f"**Antonym:** {', '.join(info['antonyms']) or '—'}")
    else:
        st.warning("Kata Tidak Ditemukan!")
