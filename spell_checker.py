from spellchecker import SpellChecker


spell = SpellChecker()

def spell_check(text):
    words = text.split() #split the text in different words
    misspelled = words.unknown(words)
    return misspelled

def suggest_corrections(word):
    return spell.candidates(word)

