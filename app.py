<<<<<<< HEAD
from dotenv import load_dotenv
import streamlit as st
import os
from google.generativeai import GenerativeModel

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize the Gemini model
gemini = GenerativeModel("gemini-pro", api_key=API_KEY)

# Streamlit UI
st.title("📚 Study Planner Chatbot")
st.write("Get a personalized study plan based on your preferences!")

# User Inputs
study_time = st.slider("How many hours per week can you study?", 1, 40, 10)
study_goal = st.selectbox("What is your study goal?", ["Semester Prep", "Interview", "Competitive Exams"])
learning_materials = st.multiselect("Preferred Learning Materials:", ["Videos", "Articles", "Books", "All"])
learning_pace = st.selectbox("Learning Pace:", ["Slow", "Moderate", "Difficult"])
specific_topics = st.text_input("Enter specific topics (e.g., Generative AI, Data Science, etc.)")

if st.button("Generate Study Plan"):
    # Prepare the prompt for Gemini API
    prompt = f"""
    Create a study plan based on the following user preferences:
    - Study Time: {study_time} hours per week
    - Study Goal: {study_goal}
    - Preferred Learning Materials: {', '.join(learning_materials) if learning_materials else 'Any'}
    - Learning Pace: {learning_pace}
    - Specific Topics: {specific_topics if specific_topics else 'General Study Plan'}
    Provide a detailed and structured study plan.
    """
    
    # Get response from Gemini API
    response = gemini.generate_text(prompt)
    
    if response:
        st.subheader("Your Personalized Study Plan:")
        st.write(response.text)
    else:
        st.error("Failed to generate a study plan. Please try again.")
=======
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai


# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize the Gemini model
genai.configure(api_key=API_KEY)  # Set up the API key
gemini = genai.GenerativeModel("gemini-pro")  # Initialize the model


# Streamlit UI
st.title("📚 Study Planner Chatbot")
st.write("Get a personalized study plan based on your preferences!")

# User Inputs
study_time = st.slider("How many hours per week can you study?", 1, 40, 10)
study_goal = st.selectbox("What is your study goal?", ["Semester Prep", "Interview", "Competitive Exams"])
learning_materials = st.multiselect("Preferred Learning Materials:", ["Videos", "Articles", "Books", "All"])
learning_pace = st.selectbox("Learning Pace:", ["Slow", "Moderate", "Difficult"])
specific_topics = st.text_input("Enter specific topics (e.g., Generative AI, Data Science, etc.)")

if st.button("Generate Study Plan"):
    # Prepare the prompt for Gemini API
    prompt = f"""
    Create a study plan based on the following user preferences:
    - Study Time: {study_time} hours per week
    - Study Goal: {study_goal}
    - Preferred Learning Materials: {', '.join(learning_materials) if learning_materials else 'Any'}
    - Learning Pace: {learning_pace}
    - Specific Topics: {specific_topics if specific_topics else 'General Study Plan'}
    Provide a detailed and structured study plan.
    """
    
    # Get response from Gemini API
    response = gemini.generate_content(prompt)  # Correct method
    
    if response:
        st.subheader("Your Personalized Study Plan:")
        st.write(response.text)
    else:
        st.error("Failed to generate a study plan. Please try again.")
>>>>>>> 7c38c47 (study)
