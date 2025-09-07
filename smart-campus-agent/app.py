import streamlit as st
from utils.hf_client import get_client
from agents.academic_agent import AcademicAgent
from agents.placement_agent import PlacementAgent
from agents.coordinator import Coordinator

# Page config
st.set_page_config(page_title="Smart Campus Assistant", page_icon="🎓", layout="centered")

st.title(" Smart Campus Assistant")
st.caption("Your academic & placement buddy, available 24/7 ⚡")

# Initialize agents
client = get_client()
academic_agent = AcademicAgent(client)
placement_agent = PlacementAgent(client)  # <-- pass client properly
coordinator = Coordinator(academic_agent, placement_agent)

# Session state to store chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Query input
query = st.text_area("Enter your question ", placeholder="E.g., Show me my timetable / How do I prepare for placements?")

col1, col2, col3 = st.columns([1, 1, 1])
response = ""

# Ask Academic
if col1.button(" Academic"):
    with st.spinner("Fetching academic info... "):
        response = coordinator.route(query, "academic")

# Ask Placement
if col2.button(" Placement"):
    with st.spinner("Fetching placement info... ⏳"):
        response = coordinator.route(query, "placement")

# Clear history
if col3.button(" Clear"):
    st.session_state.history = []
    response = ""

# Show response and save to history
if response:
    st.session_state.history.append({"query": query, "response": response})

# Display chat history
if st.session_state.history:
    st.subheader(" Chat History")
    for chat in reversed(st.session_state.history):  # latest first
        st.markdown(f"** You:** {chat['query']}")
        st.markdown(f"**Assistant:** {chat['response']}")
        st.markdown("---")
