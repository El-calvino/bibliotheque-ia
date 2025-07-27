import openai
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def demander_agent_ia(question: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o", 
            messages=[
                {"role": "system", "content": "Tu es un assistant pour une bibliothèque."},
                {"role": "user", "content": question}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Erreur lors de la requête à OpenAI : {e}"

 
def poser_question_ia(question: str, contexte: str) -> str:
    prompt = f"Contexte : {contexte}\n\nQuestion : {question}"

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Tu es un assistant qui répond de façon claire et pédagogique."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
