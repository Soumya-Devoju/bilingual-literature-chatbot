# -*- coding: utf-8 -*-
# Translation Module for Bilingual Chatbot

try:
    from googletrans import Translator
    TRANSLATION_AVAILABLE = True
except ImportError:
    TRANSLATION_AVAILABLE = False
    print("Translation library not available. Install: pip install googletrans==4.0.0rc1")

class BilingualTranslator:
    def __init__(self, target_language="es"):
        self.target_language = target_language
        if TRANSLATION_AVAILABLE:
            self.translator = Translator()
        else:
            self.translator = None
        
        self.language_names = {
            "es": "Spanish",
            "fr": "French", 
            "de": "German",
            "it": "Italian",
            "pt": "Portuguese"
        }
    
    def translate_text(self, text):
        if not TRANSLATION_AVAILABLE or not self.translator:
            # Simple fallback translations
            fallback = {
                "es": {
                    "Hello! Ask me about English literature.": "¡Hola! Pregúntame sobre literatura inglesa.",
                    "Goodbye! Happy reading!": "¡Adiós! ¡Feliz lectura!"
                }
            }
            
            if self.target_language in fallback and text in fallback[self.target_language]:
                return fallback[self.target_language][text]
            else:
                return f"[{self.target_language.upper()}]: {text}"
        
        try:
            result = self.translator.translate(text, dest=self.target_language)
            return result.text
        except Exception:
            return f"[Translation Error]: {text}"
    
    def set_target_language(self, language_code):
        self.target_language = language_code
        return f"Language changed to {self.language_names.get(language_code, language_code)}"
