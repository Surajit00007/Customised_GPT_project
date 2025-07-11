import streamlit as st
from datetime import datetime
from callolama import callOLAMA
from prompt import system_prompt  

st.set_page_config(page_title="Offline Chatbot", layout="centered")

# ---------- Sidebar: Model Selection ----------
available_models = ["phi3", "llama3", "mistral"]  # Add or remove models as needed, you need to install the LLM locally in your system before running the Chatbot.
default_model = available_models[0]

if "model" not in st.session_state:
    st.session_state.model = default_model

st.sidebar.title("Settings")
st.session_state.model = st.sidebar.selectbox("Choose a model", available_models)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": "Hello, how can I help you today?"}
    ]

if "is_typing" not in st.session_state:
    st.session_state.is_typing = False

st.title("💬 Offline LLM Chatbot")
st.markdown("Welcome to the **DEMO** of an offline GPT clone using local models.")

st.subheader("Chat Here")
for message in st.session_state.messages:
    if message["role"] == "user":
        st.info(f"You: {message['content']}")
    else:
        st.success(f"Bot: {message['content']}")

if st.session_state.is_typing:
    st.warning("The chatbot is thinking...")

st.markdown("---")
st.subheader("Your Message")

# ---------- User Input Form ----------
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message", placeholder="Ask me anything...")
    send_button = st.form_submit_button("Send message")

# ---------- Clear Chat button----------
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

if send_button and user_input.strip():
    st.session_state.messages.append({
        "role": "user",
        "content": user_input.strip()
    })

    history = system_prompt + "\n"
    for msg in st.session_state.messages:
        role = "User" if msg["role"] == "user" else "Assistant"
        history += f"{role}: {msg['content']}\n"

    full_prompt = f"{history}Assistant:"
    st.session_state.user_message = full_prompt
    st.session_state.is_typing = True
    st.rerun()

# ---------- Generate Bot Response ----------
if st.session_state.is_typing:
    user_prompt = st.session_state.user_message
    model_name = st.session_state.model

    bot_response = callOLAMA(user_prompt, model_name)

    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response
    })

    st.session_state.is_typing = False
    st.rerun()
