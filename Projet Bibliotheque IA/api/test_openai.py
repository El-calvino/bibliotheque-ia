
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Tu es un professeur."},
        {"role": "user", "content": "Explique la classe en Python."}
    ]
)

print(response.choices[0].message.content)

#pour le test on execute le fichier a partir du terminal et obtient bien une reponse
#c'est possible de changer le contexte et la requete dont on veut la reponse