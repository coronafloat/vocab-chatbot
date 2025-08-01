import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

@st.cache_data
def extract_main_keyword(text: str) -> str:
    if not text:
        return None
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalnum()]
    tokens_clean = [word for word in tokens if word.lower() not in stop_words]
    if not tokens_clean: 
        return tokens[-1].lower() if tokens else None
    tagged = pos_tag(tokens_clean)
    priority_tags = ['JJ', 'NN', 'VB']
    for tag_prefix in priority_tags:
        for word, tag in reversed(tagged):
            if tag.startswith(tag_prefix):
                return word.lower()
    return tokens_clean[-1].lower()