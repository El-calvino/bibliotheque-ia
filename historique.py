import json
import os
from datetime import datetime


class Historique:
    def __init__(self, idutilisateur, idlivre, action, date=None):
        self.idutilisateur = idutilisateur
        self.idlivre = idlivre
        self.action = action  # "emprunt" ou "retour"
        self.date = date if date else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "idutilisateur": self.idutilisateur,
            "idlivre": self.idlivre,
            "action": self.action,
            "date": self.date
        }

    def enregistrer(self, fichier="data/historique.json"):
        historique = []
        if os.path.exists(fichier):
            with open(fichier, 'r') as f:
                historique = json.load(f)
        historique.append(self.to_dict())
        with open(fichier, 'w') as f:
            json.dump(historique, f, indent=4)