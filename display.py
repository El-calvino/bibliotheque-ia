import json
import os


def afficher_livres_disponibles(fichier="data/bibliotheque.json"):
    if not os.path.exists(fichier):
        print("📭 Aucun livre trouvé.")
        return

    with open(fichier, 'r') as f:
        livres = json.load(f)

    disponibles = [livre for livre in livres if livre.get("disponible", True)]

    if not disponibles:
        print("📕 Aucun livre disponible actuellement.")
    else:
        print("\n📚 Livres disponibles :")
        for livre in disponibles:
            print(f"  ID: {livre['idlivre']} | {livre['titre']} - {livre['auteur']}")


def afficher_historique(idutilisateur, fichier="data/historique.json"):
    if not os.path.exists(fichier):
        print("🕳️ Aucun historique trouvé.")
        return

    with open(fichier, 'r') as f:
        historique = json.load(f)

    user_hist = [h for h in historique if h["idutilisateur"] == idutilisateur]

    if not user_hist:
        print("📭 Aucun emprunt/retour enregistré pour cet utilisateur.")
    else:
        print("\n🕘 Historique de vos activités :")
        for h in user_hist:
            print(f"{h['date']} | Livre ID: {h['idlivre']} | Action: {h['action']}")
