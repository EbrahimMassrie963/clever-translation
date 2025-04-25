import os
import requests
import json
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.app.db.session import SessionLocal  
from backend.app.db.models import TranslationRequest
from backend.app.schemas.translation import TranslationRequestSchema, TranslationResponseSchema
from backend.app.core.config import settings  

router = APIRouter()  

API_KEY = settings.GEMINI_API_KEY

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/translate", response_model=TranslationResponseSchema)
async def create_translation(request: TranslationRequestSchema, db: Session = Depends(get_db)):
    """Handles translation requests"""
    
    input_text = request.input_text
    target_languages = request.target_languages

    db_translation = TranslationRequest(input_text=input_text, target_languages=target_languages)
    db.add(db_translation)
    db.commit()
    db.refresh(db_translation)

    languages_list = [lang.strip() for lang in target_languages.split(",")]

    translations = {}
    for lang in languages_list:
        try:
            translated_text = await translate_using_gemini(input_text, lang)
            translations[lang] = translated_text
        except Exception as e:
            translations[lang] = f"Error translating to {lang}: {str(e)}"

    db_translation.translated_text = json.dumps(translations)
    db.commit()
    return {"message": "Translation request successfully submitted!", "translations": translations}

async def translate_using_gemini(input_text: str, target_language: str) -> str:
    """Communicates with Gemini API to get translations"""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    
    prompt = f"Translate the following text to {target_language}. Return only the translated text with no explanations, examples, or additional context:\n\n{input_text}"

    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        result = response.json()
        return result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "Translation not found").strip()
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")

