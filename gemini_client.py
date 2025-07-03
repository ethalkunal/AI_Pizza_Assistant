import os
from dotenv import load_dotenv
import google.generativeai as genai
from google.generativeai import GenerationConfig
from utils import build_order_prompt
from menu import menu, toppings

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

def get_ai_reply(user_message, conversation):
    system_prompt = build_order_prompt(menu, toppings)

    # Gemini only supports "user" and "model" roles
    full_convo = [{"role": "user", "parts": [system_prompt]}]
    full_convo += [{"role": "user", "parts": [msg]} if i % 2 == 0 else {"role": "model", "parts": [msg]}
                   for i, msg in enumerate(conversation + [user_message])]

    response = model.generate_content(
        contents=full_convo,
        generation_config=GenerationConfig(max_output_tokens=1000)
    )

    if not response.candidates or not response.candidates[0].content.parts:
        return "⚠️ I didn't understand that. Please try rephrasing.", conversation

    return response.text, conversation + [user_message, response.text]
