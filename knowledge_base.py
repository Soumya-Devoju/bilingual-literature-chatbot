# -*- coding: utf-8 -*-
# Literature Knowledge Base for Bilingual Chatbot

class LiteratureKnowledgeBase:
    def __init__(self):
        self.literature_data = {
            "shakespeare": {
                "keywords": ["shakespeare", "hamlet", "romeo", "juliet", "macbeth", "othello"],
                "responses": [
                    "Shakespeare is considered the greatest English playwright. His works include Hamlet, Romeo and Juliet, and Macbeth.",
                    "William Shakespeare (1564-1616) wrote approximately 37 plays and 154 sonnets.",
                    "Shakespeare tragedies explore themes of power, love, betrayal, and human nature."
                ]
            },
            "austen": {
                "keywords": ["austen", "pride", "prejudice", "emma", "persuasion"],
                "responses": [
                    "Jane Austen wrote novels about social commentary in Regency England.",
                    "Pride and Prejudice is Austen most famous work featuring Elizabeth Bennet and Mr. Darcy.",
                    "Austen novels are known for their wit and strong female protagonists."
                ]
            },
            "dickens": {
                "keywords": ["dickens", "christmas carol", "oliver twist", "great expectations"],
                "responses": [
                    "Charles Dickens was a Victorian novelist known for social criticism.",
                    "A Christmas Carol tells the story of Ebenezer Scrooge transformation.",
                    "Dickens novels featured poor working conditions and social inequality."
                ]
            },
            "orwell": {
                "keywords": ["orwell", "1984", "animal farm", "big brother"],
                "responses": [
                    "George Orwell wrote dystopian novels like 1984 and Animal Farm.",
                    "1984 explores themes of totalitarianism, surveillance, and thought control.",
                    "Animal Farm is an allegory about the Russian Revolution."
                ]
            }
        }
    
    def get_topic_data(self, topic):
        return self.literature_data.get(topic, None)
