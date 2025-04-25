from pydantic import BaseModel

class TranslationRequestSchema(BaseModel):
    """Schema for translation request"""
    input_text: str
    target_languages: str  

class TranslationResponseSchema(BaseModel):
    """Schema for translation response"""
    message: str
    translations: dict  
