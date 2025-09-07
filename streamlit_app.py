# -*- coding: utf-8 -*-
import streamlit as st
from main import BilingualLiteratureChatbot

st.set_page_config(page_title="Bilingual Literature Chatbot", page_icon="📚")

if 'chatbot' not in st.session_state:
    st.session_state.chatbot = BilingualLiteratureChatbot(target_language='es')

if 'messages' not in st.session_state:
    st.session_state.messages = []

st.title("🌍 Bilingual Literature Chatbot")
st.write("Chat about English literature and get responses in two languages!")

# Language selector
language_options = {'Spanish': 'es', 'French': 'fr', 'German': 'de', 'Italian': 'it', 'Portuguese': 'pt'}
selected_language = st.selectbox("Choose response language:", options=list(language_options.keys()))
st.session_state.chatbot.translator.set_target_language(language_options[selected_language])

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me about English literature..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        response = st.session_state.chatbot.get_bilingual_response(prompt)
        
        bot_message = f"**English:** {response['english']}\n\n**{selected_language}:** {response['translated']}"
        st.markdown(bot_message)
        
        st.session_state.messages.append({"role": "assistant", "content": bot_message})
