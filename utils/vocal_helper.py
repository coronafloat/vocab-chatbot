from nltk.corpus import wordnet
from itertools import islice

def get_word_info(word: str, max_examples: int = 3):
    synsets = wordnet.synsets(word)
    if not synsets:
        return None

    definition = next(iter(synsets)).definition()

    # Examples
    examples = (ex for syn in synsets for ex in syn.examples())
    examples = list(dict.fromkeys(islice(examples, max_examples)))
    if not examples:
        examples = ["Example Sentences Are Not Available😣"]

    # Synonyms & Antonyms
    synonyms, antonyms = set(), set()
    for syn in synsets:
        for lemma in syn.lemmas():
            synonyms.add(lemma.name().replace('_', ' '))
            antonyms.update(ant.name().replace('_', ' ') for ant in lemma.antonyms() if ant)

    synonyms = list(synonyms)[:5]
    antonyms = list(antonyms)[:5]

    return {
        "definition": definition,
        "examples": examples,
        "synonyms": synonyms,
        "antonyms": antonyms,
    }
