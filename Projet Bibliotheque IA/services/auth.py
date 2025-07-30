import json
import os
from models.utilisateur import Utilisateur
from models.employes import Employe


def connexion_utilisateur(login, motdepasse, fichier="data/utilisateurs.json"):
    if not os.path.exists(fichier):
        print(" Aucun utilisateur enregistré.")
        return None

    with open(fichier, 'r') as f:
        utilisateurs = json.load(f)
        for user in utilisateurs:
            if user["login"] == login and user["motdepasse"] == motdepasse:
                print(f" Bienvenue {user['prenom']} {user['nom']} !")
                return Utilisateur(
                    user["nom"], user["prenom"], user["adresse"], user["phone"],
                    user["age"], user["statut"], user["idutilisateur"], user["login"], user["motdepasse"]
                )
    print(" Login ou mot de passe incorrect.")
    return None


def connexion_employe(login, motdepasse, fichier="data/employes.json"):
    if not os.path.exists(fichier):
        print(" Aucun employé enregistré.")
        return None

    with open(fichier, 'r') as f:
        employes = json.load(f)
        for emp in employes:
            if emp["login"] == login and emp["motdepasse"] == motdepasse:
                print(f" Connexion réussie. Bienvenue {emp['prenom']} {emp['nom']}")
                return Employe(
                    emp["nom"], emp["prenom"], emp["adresse"], emp["phone"], emp["age"], emp["statut"],
                    emp["idemploye"], emp["shift"], emp["NAS"], emp["login"], emp["motdepasse"]
                )
    