# -*- coding: utf-8 -*-
# Complete Bilingual Literature Chatbot

import random
from knowledge_base import LiteratureKnowledgeBase
from translator import BilingualTranslator

class BilingualLiteratureChatbot:
    def __init__(self, target_language="es"):
        self.knowledge_base = LiteratureKnowledgeBase()
        self.translator = BilingualTranslator(target_language)
        
        self.greetings = {
            "patterns": ["hello", "hi", "hey", "greetings"],
            "responses": [
                "Hello! I am here to help you with English literature questions.",
                "Hi! Ask me about English books, authors, and literary themes.",
                "Welcome! I can discuss English literature and provide bilingual responses."
            ]
        }
        
        self.farewells = {
            "patterns": ["bye", "goodbye", "farewell", "quit", "exit"],
            "responses": [
                "Goodbye! Happy reading!",
                "Farewell! Keep exploring literature!",
                "See you later! Literature opens many worlds."
            ]
        }
    
    def find_best_response(self, user_input):
        input_lower = user_input.lower()
        
        if any(greeting in input_lower for greeting in self.greetings["patterns"]):
            return random.choice(self.greetings["responses"]), "greeting"
        
        if any(farewell in input_lower for farewell in self.farewells["patterns"]):
            return random.choice(self.farewells["responses"]), "farewell"
        
        best_score = 0
        best_response = "I can help with questions about Shakespeare, Austen, Dickens, Orwell and other English authors."
        best_category = "unknown"
        
        for topic, data in self.knowledge_base.literature_data.items():
            score = 0
            for keyword in data["keywords"]:
                if keyword in input_lower:
                    score += 1
            
            if score > best_score:
                best_score = score
                best_response = random.choice(data["responses"])
                best_category = topic
        
        return best_response, best_category
    
    def get_bilingual_response(self, user_input):
        english_response, category = self.find_best_response(user_input)
        translated_response = self.translator.translate_text(english_response)
        
        return {
            "english": english_response,
            "translated": translated_response,
            "category": category,
            "target_language": self.translator.target_language
        }
    
    def chat(self):
        print("=== Bilingual Literature Chatbot ===")
        print("Ask me about English literature! Type 'quit' to exit.")
        
        while True:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ["quit", "exit"]:
                farewell = self.get_bilingual_response("goodbye")
                print(f"Bot (EN): {farewell['english']}")
                print(f"Bot ({farewell['target_language'].upper()}): {farewell['translated']}")
                break
            
            response = self.get_bilingual_response(user_input)
            print(f"Bot (EN): {response['english']}")
            print(f"Bot ({response['target_language'].upper()}): {response['translated']}")
            print()

if __name__ == "__main__":
    chatbot = BilingualLiteratureChatbot(target_language="es")
    chatbot.chat()
