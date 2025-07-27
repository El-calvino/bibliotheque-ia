from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .openai_integration import demander_agent_ia
from .openai_integration import poser_question_ia  
import json
import os

app = FastAPI(title="API Bibliothèque IA [Emeraude-Freedy-Calvin]")

DATA_DIR = "data"

class Question(BaseModel):
    texte: str


class QuestionIA(BaseModel):
    question: str
    contexte: str

def charger_fichier_json(nom_fichier):
    path = os.path.join(DATA_DIR, nom_fichier)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail=f"Fichier {nom_fichier} introuvable.")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

@app.get("/")
def root():
    return {"Message": "Bienvenue sur l'API de la bibliothèque, realise par Emeraude, Freedy et Calvin"}

@app.get("/livres/")
def get_livres_disponibles():
    path = os.path.join(DATA_DIR, "bibliotheque.json")
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Fichier bibliothèque introuvable.")
    
    with open(path, "r") as f:
        livres = json.load(f)

    livres_disponibles = [livre for livre in livres if livre.get("disponible", True)]
    return {"livres_disponibles": livres_disponibles}


@app.get("/employes/")
def get_employes():
    employes = charger_fichier_json("employes.json")
    return {"employes": employes}

@app.get("/employes/{id_employe}")
def get_employe_par_id(id_employe: str):
    employes = charger_fichier_json("employes.json")
    for emp in employes:
        if emp.get("idemploye") == id_employe:
            return emp
    raise HTTPException(status_code=404, detail="Employé non trouvé")

@app.get("/utilisateurs/")
def get_utilisateurs():
    utilisateurs = charger_fichier_json("utilisateurs.json")
    return {"utilisateurs": utilisateurs}

@app.get("/utilisateurs/{id_utilisateur}")
def get_utilisateur_par_id(id_utilisateur: str):
    utilisateurs = charger_fichier_json("utilisateurs.json")
    for util in utilisateurs:
        if util.get("idutilisateur") == id_utilisateur:
            return util
    raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

@app.get("/historique/")
def get_historique():
    historique = charger_fichier_json("historique.json")
    return {"historique": historique}

@app.post("/ia/")
def question_ia(question: Question):
    reponse = demander_agent_ia(question.texte)
    return {"réponse": reponse}

@app.post("/interaction-ia/")  
def interaction_ia(data: QuestionIA):
    reponse = poser_question_ia(data.question, data.contexte)
    return {"reponse": reponse}