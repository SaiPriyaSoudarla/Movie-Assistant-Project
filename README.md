# 🎬 Movie Assistant

**Movie Assistant** is an AI-powered web application that helps users quickly get concise summaries of movies and discover similar titles. Built with **Streamlit** and powered by **Google's Gemini (Generative AI)**, the app delivers fast, intelligent, and engaging responses for movie lovers.

---

## 📌 Problem Statement

Finding quick and reliable information about movies—including summaries and recommendations—often requires browsing multiple websites. This can be time-consuming and frustrating. There’s a need for a simple, intelligent assistant that provides both a movie's summary and similar recommendations instantly.

---

## 💡 Proposed Solution

This project presents a **Streamlit-based web app** that utilizes **Google's Gemini API** to provide:
- A short summary of the given movie.
- 3–5 similar movies based on genre, theme, or concept.

With a minimal and user-friendly UI, users can explore new movies in seconds with just one input.

---

## 🧱 System Development Approach

### 🎨 Frontend
- Built with **Streamlit**
- Accepts user input and displays AI-generated responses
- Includes loading spinner and error handling

### 🤖 Backend
- Uses **Google Generative AI (Gemini 1.5 Flash)** to generate content
- Constructs a detailed prompt dynamically from user input
- Parses and displays response text

### 🔐 Environment Handling
- `.env` file to store API key securely
- `python-dotenv` for environment variable management

---

## ⚙️ Algorithm & Deployment

### 🧠 Algorithm
1. Take movie name as input.
2. Generate a prompt asking Gemini to provide a summary and recommendations.
3. Call `generate_content()` from Gemini API.
4. Format and display the response.

### 🚀 Deployment
Run the following in your terminal:
```bash
streamlit run movie_assistant.py



