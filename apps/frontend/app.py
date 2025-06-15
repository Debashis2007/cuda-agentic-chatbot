import streamlit as st
import requests

st.set_page_config(page_title="Agentic AI Chatbot", layout="centered")

st.title("🤖 Agentic AI Chatbot")

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

user_input = st.text_input("You:", "", key="input")

if st.button("Send") and user_input:
    st.session_state['messages'].append({"role": "user", "content": user_input})

    response = requests.post("http://backend:8000/chat", json={"message": user_input})
    bot_response = response.json().get("response", "No response from server.")

    st.session_state['messages'].append({"role": "bot", "content": bot_response})

for msg in st.session_state['messages']:
    if msg['role'] == 'user':
        st.write(f"**You:** {msg['content']}")
    else:
        st.write(f"**Bot:** {msg['content']}")