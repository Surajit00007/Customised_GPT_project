import streamlit as st
import requests
import json
from datetime import datetime
from callolama import callOLAMA  # Make sure callolama.py is in same folder

st.set_page_config(page_title="Chatbot")

# Select Model
available_models = ["phi3", "llama3", "mistral"]  
default_model = available_models[0]

if "model" not in st.session_state:
    st.session_state.model = default_model

st.sidebar.title("Settings")
st.session_state.model = st.sidebar.selectbox("Choose a model", available_models)


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": "Hello, how can I help you today?"}
    ]

if "is_typing" not in st.session_state:
    st.session_state.is_typing = False

# UI Title and Intro
st.title("Offline LLM")
st.markdown("Welcome to DEMO of Offline GPT")
st.subheader("Chat Here")

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.info(message["content"])
    else:
        st.success(message["content"])

if st.session_state.is_typing:
    st.markdown("The ChatBot is thinking...")
    st.warning("Typing...")

st.markdown("---")
st.subheader("Your message")

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message", placeholder="Ask me anything...")
    send_button = st.form_submit_button("Send message")

# Clear button
col1, col2 = st.columns([1, 1])
with col1:
    clear_button = st.button("Clear Chat")

if clear_button:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": "Hello, how can I help you today?"}
    ]
    st.rerun()

# Handle user message
if send_button and user_input.strip():
    st.session_state.messages.append({
        "role": "user",
        "content": user_input.strip()})
    
    st.session_state.is_typing = True
    st.rerun()

# Process bot response
if st.session_state.is_typing:
    user_message = st.session_state.messages[-1]["content"]
    
    bot_response = callOLAMA(user_message, st.session_state.model)

    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response})
    
    st.session_state.is_typing = False
    st.rerun()
