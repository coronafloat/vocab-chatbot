from nltk.corpus import wordnet

def get_word_info(word: str, max_examples: int = 3):
    synsets = wordnet.synsets(word)
    if not synsets:
        return None

    # ── definisi & contoh ────────────────────────────────────────────────
    definition = synsets[0].definition()

    # kumpulkan semua contoh unik, batasi ke 'max_examples'
    examples = []
    for syn in synsets:
        for ex in syn.examples():
            if ex not in examples:
                examples.append(ex)
            if len(examples) >= max_examples:
                break
        if len(examples) >= max_examples:
            break
    if not examples:
        examples = ["Contoh tidak tersedia."]

    # ── sinonim & antonim ────────────────────────────────────────────────
    synonyms, antonyms = set(), set()
    for syn in synsets:
        for lemma in syn.lemmas():
            synonyms.add(lemma.name().replace('_', ' '))
            if lemma.antonyms():
                antonyms.add(lemma.antonyms()[0].name().replace('_', ' '))

    return {
        "definition": definition,
        "examples": examples,          # ← list, bukan string tunggal
        "synonyms": list(synonyms)[:5],
        "antonyms": list(antonyms)[:5],
    }
