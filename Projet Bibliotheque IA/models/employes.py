import json
import os
from models.humain import Humain
from models.livre import Livre  # utile pour manipulation dans les menus


class Employe(Humain):
    def __init__(self, nom, prenom, adresse, phone, age, statut, idemploye, shift, NAS, login, motdepasse):
        super().__init__(nom, prenom, adresse, phone, age, statut)
        self.idemploye = idemploye
        self.shift = shift
        self.NAS = NAS
        self.login = login
        self.motdepasse = motdepasse

    def to_dict(self):     #cette fonction permet de convertir les infos recues pour les stocker dans un fichier json
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "adresse": self.adresse,
            "phone": self.phone,
            "age": self.age,
            "statut": self.statut,
            "idemploye": self.idemploye,
            "shift": self.shift,
            "NAS": self.NAS,
            "login": self.login,
            "motdepasse": self.motdepasse
        }

    def enregistrer_employe(self, fichier="data/employes.json"):
        employes = self._charger_employes(fichier)
        if any(emp["login"] == self.login for emp in employes):
            print(" Ce login est déjà utilisé.")
            return
        employes.append(self.to_dict())
        self._sauvegarder_employes(employes, fichier)
        print(f" Employé {self.nom} enregistré avec succès.")

    def _charger_employes(self, fichier):
        if os.path.exists(fichier):
            with open(fichier, 'r') as f:
                return json.load(f)
        else:
            return []

    def _sauvegarder_employes(self, employes, fichier):
        with open(fichier, 'w') as f:
            json.dump(employes, f, indent=4)

    def Ajouterlivre(self, livre, fichier="data/bibliotheque.json"):
        bibliotheque = self._charger_bibliotheque(fichier)
        bibliotheque.append(livre.to_dict())
        self._sauvegarder_bibliotheque(bibliotheque, fichier)
        print(f" Livre '{livre.titre}' ajouté avec succès.")

    def Retirerlivre(self, idlivre, fichier="data/bibliotheque.json"):
        bibliotheque = self._charger_bibliotheque(fichier)
        bibliotheque = [livre for livre in bibliotheque if livre["idlivre"] != idlivre]
        self._sauvegarder_bibliotheque(bibliotheque, fichier)
        print(f" Livre avec ID {idlivre} retiré avec succès.")

    def AfficherBibliotheque(self, fichier="data/bibliotheque.json"):
        bibliotheque = self._charger_bibliotheque(fichier)
        if not bibliotheque:
            print(" La bibliothèque est vide.")
        else:
            print("\n Livres disponibles :")
            for livre in bibliotheque:
                print(f"  ID: {livre['idlivre']} | {livre['titre']} par {livre['auteur']}")

    def _charger_bibliotheque(self, fichier):
        if os.path.exists(fichier):
            with open(fichier, 'r') as f:
                return json.load(f)
        else:
            return []

    def _sauvegarder_bibliotheque(self, bibliotheque, fichier):
        with open(fichier, 'w') as f:
            json.dump(bibliotheque, f, indent=4)