
try:
    from googletrans import Translator
except ImportError:
    Translator = None

french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
english_words = ["Hello", "Goodbye", "Welcome", "See you soon"]
french_to_english = dict(zip(french_words, english_words))

# Use local dictionary fallback if googletrans is not available
translator = Translator() if Translator else None

def translate_to_english(french_word):
    if translator:
        translation = translator.translate(french_word, src='fr', dest='en')
        return translation.text
    return french_to_english.get(french_word, f"Translation for '{french_word}' not found")
# Example usage
french_word = "Bonjour"
english_translation = translate_to_english(french_word)
print(f"The English translation of '{french_word}' is: '{english_translation}'")
