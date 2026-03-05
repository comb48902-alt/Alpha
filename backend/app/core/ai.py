import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

async def chat_with_m(message: str, history: list = []):
    messages = [
        {"role": "system", "content": "أنت M - مساعد ذكاء اصطناعي أمني متخصص. أنت تعمل داخل منظومة ALPHA. ساعد صاحبك في كل ما يحتاج."}
    ] + history + [{"role": "user", "content": message}]
    
    response = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=messages,
        max_tokens=1000
    )
    return response.choices[0].message.content
