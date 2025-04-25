from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class TranslationRequest(Base):
    __tablename__ = "translation_requests"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    input_text = Column(Text, nullable=False)  
    target_languages = Column(String, nullable=False)  
    translated_text = Column(Text, nullable=True)  
    created_at = Column(DateTime, default=datetime.utcnow)  

