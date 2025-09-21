import streamlit as st
import datetime

# ---- Title ----
st.title("GenWell AI 🧠💬")
st.subheader("Your Compassionate AI Confidant")

# ---- Mood Tracker ----
st.header("🌈 Mood Tracker")
mood = st.radio("How are you feeling today?", ["😊 Happy", "😔 Sad", "😟 Stressed", "😴 Tired", "😎 Excited"])
if st.button("Save Mood"):
    st.success(f"✅ Your mood '{mood}' has been saved for today ({datetime.date.today()}).")

# ---- Journal ----
st.header("📔 Daily Journal")
journal = st.text_area("Write your thoughts here...")
if st.button("Save Journal"):
    st.success("✅ Your journal entry has been saved (demo storage).")

# ---- AI Chatbot (Demo) ----
st.header("💬 Chat with GenWell AI")
user_input = st.text_input("You:", "")
if user_input:
    # For now, give a simple demo reply
    st.text_area("GenWell AI:", f"I hear you. It sounds like '{user_input}'. Remember, it's okay to feel this way. 🌱", height=100)
