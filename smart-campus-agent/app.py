# app.py

import streamlit as st
from utils.hf_client import get_client
from agents.academic_agent import AcademicAgent
from agents.placement_agent import PlacementAgent
from agents.coordinator import Coordinator

st.set_page_config(page_title="Smart Campus Assistant", page_icon="", layout="centered")

st.title(" Smart Campus Assistant")
st.caption("Your academic & placement buddy, available 24/7 ")

client = get_client()
academic_agent = AcademicAgent(client)
placement_agent = PlacementAgent(client)
coordinator = Coordinator(academic_agent, placement_agent)

if "history" not in st.session_state:
    st.session_state.history = []

query = st.text_area("Enter your question ", placeholder="how can i help you?")
response = ""

if st.button(" Ask Assistant"):
    with st.spinner("Thinking... "):
        response = coordinator.route(query)

# Clear history
if st.button(" Clear"):
    st.session_state.history = []
    response = ""

# Save response
if response:
    st.session_state.history.append({"query": query, "response": response})

# Display history
if st.session_state.history:
    st.subheader("Chat History")
    for chat in reversed(st.session_state.history):
        st.markdown(f"** You:** {chat['query']}")
        st.markdown(f"** Assistant:** {chat['response']}")
        st.markdown("---")
    st.button(" Clear History", on_click=lambda: st.session_state.history.clear())
    