from fastapi import FastAPI, HTTPException, Body
from google import genai
from google.genai import types
from ai_endpoint.constants import *
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
@app.post("/chat/")
async def chat_raw(user_input: str = Body(..., media_type="text/plain")):
    try:
        gemini_api = os.environ.get("GEMINI_API_KEY")
        ai_client = genai.Client(api_key=gemini_api)
        contents = types.Content(role='user', parts=[types.Part.from_text(text=f"{user_input}")])

        reply = ai_client.models.generate_content(
        model="gemini-2.5-flash", contents=contents,
        config=types.GenerateContentConfig(
            system_instruction=f"{SHOPPING_HELPER_INSTRUCTION}",
            max_output_tokens=3000,
            top_k=25,
            top_p=0.9,
            temperature=0.9,
            response_mime_type='application/json',
            stop_sequences=['\n']
            )
        )
        return {"response": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))