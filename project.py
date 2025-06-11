import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to get summary and recommendations
def get_movie_summary_and_recs(movie_name):
    prompt = f"""
    Tell me what the movie "{movie_name}" is about in 3-4 sentences.
    Also recommend 3-5 similar movies based on its theme, genre, or concept.
    Format output clearly with 'Summary:' and 'Similar Movies:' sections.
    """
    response = model.generate_content(prompt)
    return response.text.strip()

# Streamlit UI
st.title("🎬Movie Assistant")
movie_input = st.text_input("Enter a movie name:")

if st.button("Generate Summary & Recommendations"):
    if movie_input.strip():
        with st.spinner("Thinking..."):
            result = get_movie_summary_and_recs(movie_input)
        st.subheader("📖 Gemini Response")
        st.write(result)
    else:
        st.warning("Please enter a movie name.")
