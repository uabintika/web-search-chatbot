import streamlit as st
import asyncio
from agent_runner import run_agent

st.set_page_config(page_title="Web Search Chatbot", layout="centered")
st.title("Web Search Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask something...", placeholder="e.g. What is the capital of Lithuania?", key="input")

if st.button("Ask") and user_input.strip():
    with st.spinner("Thinking..."):
        output = asyncio.run(run_agent(user_input))
        st.session_state.chat_history.append((user_input, output))

st.divider()
st.markdown("### Chat History")
for i, (q, a) in enumerate(reversed(st.session_state.chat_history), 1):
    st.markdown(f"**You:** {q}")
    st.markdown(f"**Agent:** {a}")