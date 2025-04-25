# Gemini Translation API

A robust translation service that integrates with the Gemini API to provide multi-language translations. The project supports FastAPI for the backend, PostgreSQL for the database, and a basic HTML/JS frontend to interact with the API. The application allows users to submit text in one language and receive translations in multiple languages.

---

## Features

- **Text Translation:** Translates text into multiple languages (Arabic, French, Spanish, etc.) using the Gemini API.
- **Database Integration:** Stores translation logs in a PostgreSQL database.
- **Frontend:** Simple web interface for interacting with the API.
- **CORS Support:** Handles cross-origin requests to allow frontend interactions with the backend.

---

## Project Structure

Translation using Gemini flash 1.5/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── endpoints/
│   │   │       └── translate.py
│   │   ├── core/
│   │   │   └── config.py
│   │   ├── db/
│   │   │   ├── models.py
│   │   │   └── session.py
│   │   ├── schemas/
│   │   │   └── translation.py
│   │   └── main.py
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── js/
│   │       └── script.js
│   └── index.html
├── .env
├── requirements.txt
---

## Requirements

- Python 3.8+
- FastAPI for the backend
- PostgreSQL for the database
- Jinja2 for HTML templating
- psycopg2 for PostgreSQL integration
- requests for making HTTP requests
- python-dotenv for managing environment variables

---

## Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/clever-translation
    cd clever-translation
    ```

2. **Set up the virtual environment**
    ```bash
    python -m venv venv
    ```
    - For Linux/macOS:
      ```bash
      source venv/bin/activate
      ```
    - For Windows:
      ```bash
      venv\Scripts\activate
      ```

3. **Install the dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the environment variables**

    Create a `.env` file in the root directory and set the following environment variables:

    ```
    DATABASE_URL=postgresql://postgres:password@localhost/Gemini_translation_db
    GEMINI_API_KEY=your_gemini_api_key_here
    ```

    Replace `your_gemini_api_key_here` with your actual Gemini API key.

5. **Run the application**

    You can run the backend using Uvicorn:

    ```bash
    uvicorn backend.app.main:app --reload
    ```

    - Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to access the backend API.
    - To check if the application is working, visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for the auto-generated API documentation by FastAPI.

---

## Using the Application

1. **Send a Translation Request**

    The frontend is located in the `frontend/` directory. Open the `index.html` file in your browser.

    You can input the text you want to translate and select the target languages. Upon submission, the frontend sends a POST request to the backend API at `http://127.0.0.1:8000/translate`.

2. **Example Request Payload**

    The API expects the following JSON format:

    ```json
    {
        "input_text": "Hello, how are you?",
        "target_languages": "Arabic, French, Spanish"
    }
    ```

    The backend will respond with the translated text for each requested language:

    ```json
    {
        "message": "Translation request successfully submitted!",
        "translations": {
            "Arabic": "مرحبا، كيف حالك؟",
            "French": "Bonjour, comment allez-vous ?",
            "Spanish": "Hola, ¿cómo estás?"
        }
    }
    ```

3. **CORS**

    If you encounter CORS issues, ensure that you have properly set up the `CORSMiddleware` in FastAPI as shown in the project structure.

---

## Database Setup

The database is set up automatically when the application starts if it does not already exist. The backend connects to PostgreSQL using the `DATABASE_URL` defined in your `.env` file.

If the database does not exist, it will be created automatically.

---


Troubleshooting
If you encounter any issues, try the following:

Ensure that PostgreSQL is running and that the DATABASE_URL is correctly set.
Make sure that the Gemini API key is valid and correctly set in the .env file.
If the frontend does not load, check if your static files are correctly served and that the StaticFiles mount is correctly set up in main.py.


