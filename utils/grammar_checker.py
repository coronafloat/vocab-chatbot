import os
import replicate
import streamlit as st

def check_grammar(text: str) -> str:
    replicate_token = st.secrets["REPLICATE_API_TOKEN"]
    os.environ["REPLICATE_API_TOKEN"] = replicate_token

    prompt = (
        f"Correct the grammar of the following sentence. "
        f"Only return the corrected sentence, without any explanation or comments. "
        f"This is the sentence:\n\n{text}"
    )

    output = replicate.run(
        "ibm-granite/granite-3.3-8b-instruct",
        input={
            "prompt": prompt
        }
    )

    return "".join(output).strip() if isinstance(output, list) else str(output).strip()
