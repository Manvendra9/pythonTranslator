from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class TranslationRequest(BaseModel):
    code: str
    language: str

# Placeholder function to simulate translation
def translate_code(code: str, language: str) -> str:
    return f"# Translated Python code to {language.upper()}:\n{code}"

@app.post("/translate")
async def translate(request: TranslationRequest) -> Dict[str, str]:
    if not request.code.strip():
        raise HTTPException(status_code=400, detail="Code cannot be empty")
    
    translated_code = translate_code(request.code, request.language)
    return {"translatedCode": translated_code}
