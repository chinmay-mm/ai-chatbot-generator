# AI Chatbot Generator

A simple AI-powered chatbot web application built with Python and Flask. Users can interact with the chatbot through a clean chat interface, and the bot responds intelligently using keyword-based intent matching (NLP-style logic).

## Features
- Real-time chat interface with a clean, responsive UI
- Keyword/intent-based response engine (handles greetings, hours, pricing, contact info, etc.)
- Built with Flask backend and vanilla JS frontend
- Easily extendable — add new intents/responses by updating a simple dictionary

## Tech Stack
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Logic:** Rule-based NLP (keyword/intent matching)

## How to Run
1. Clone the repository
2. Install dependencies: `pip install flask`
3. Run the app: `python app.py`
4. Open `http://127.0.0.1:5000` in your browser

## Future Improvements
- Integrate a proper NLP library (e.g., NLTK or spaCy) for smarter intent detection
- Add conversation history/context handling
- Deploy to a cloud platform (Render/Heroku)
