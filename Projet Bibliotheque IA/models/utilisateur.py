import json
import os
from models.humain import Humain
from models.historique import Historique





class Utilisateur(Humain):
    def __init__(self, nom, prenom, adresse, phone, age, statut, idutilisateur, login, motdepasse):
        super().__init__(nom, prenom, adresse, phone, age, statut)
        self.idutilisateur = idutilisateur
        self.login = login
        self.motdepasse = motdepasse

    def to_dict(self):
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "adresse": self.adresse,
            "phone": self.phone,
            "age": self.age,
            "statut": self.statut,
            "idutilisateur": self.idutilisateur,
            "login": self.login,
            "motdepasse": self.motdepasse
        }

    def enregistrer_utilisateur(self, fichier="data/utilisateurs.json"):
        utilisateurs = self._charger_utilisateurs(fichier)
        if any(user["login"] == self.login for user in utilisateurs):
            print(" Ce login est déjà utilisé.")
            return
        utilisateurs.append(self.to_dict())
        self._sauvegarder_utilisateurs(utilisateurs, fichier)
        print(f" Utilisateur {self.nom} enregistré avec succès.")

    def _charger_utilisateurs(self, fichier):
        if os.path.exists(fichier):
            with open(fichier, 'r') as f:
                return json.load(f)
        return []

    def _sauvegarder_utilisateurs(self, utilisateurs, fichier):
        with open(fichier, 'w') as f:
            json.dump(utilisateurs, f, indent=4)

    def emprunter_livre(self, idlivre, fichier="data/bibliotheque.json"):
        if not os.path.exists(fichier):
            print(" Aucun livre disponible.")
            return

        with open(fichier, 'r') as f:
            livres = json.load(f)

        for livre in livres:
            if livre["idlivre"] == idlivre:
                if livre.get("disponible", True):
                    livre["disponible"] = False
                    with open(fichier, 'w') as f:
                        json.dump(livres, f, indent=4)
                    print(f" Livre '{livre['titre']}' emprunté avec succès.")
                    Historique(self.idutilisateur, idlivre, "emprunt").enregistrer()
                    return
                else:
                    print(" Ce livre est déjà emprunté.")
                    return
        print(" Livre non trouvé.")

    def retourner_livre(self, idlivre, fichier="data/bibliotheque.json"):
        if not os.path.exists(fichier):
            print(" Aucun livre enregistré.")
            return

        with open(fichier, 'r') as f:
            livres = json.load(f)

        for livre in livres:
            if livre["idlivre"] == idlivre:
                if not livre.get("disponible", True):
                    livre["disponible"] = True
                    with open(fichier, 'w') as f:
                        json.dump(livres, f, indent=4)
                    print(f" Livre '{livre['titre']}' retourné avec succès.")
                    Historique(self.idutilisateur, idlivre, "retour").enregistrer()
                    return
                else:
                    print(" Ce livre n'était pas emprunté.")
                    return
        print(" Livre non trouvé.")