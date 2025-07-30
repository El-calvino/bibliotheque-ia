from services.auth import connexion_employe, connexion_utilisateur
from models.utilisateur import Utilisateur
from models.employes import Employe
from services.display import afficher_livres_disponibles, afficher_historique

def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Connexion Employé")
        print("2. Connexion Utilisateur")
        print("3. Enregistrement Utilisateur")
        print("4. Enregistrement Employé")
        print("0. Quitter")

        choix = input("Ton choix : ")

        if choix == "1":
            login = input("Login employé : ")
            motdepasse = input("Mot de passe : ")
            employe = connexion_employe(login, motdepasse)
            if employe:
                menu_employe(employe)
            else:
                print(" Identifiants incorrects.")

        elif choix == "2":
            login = input("Login utilisateur : ")
            motdepasse = input("Mot de passe : ")
            utilisateur = connexion_utilisateur(login, motdepasse)
            if utilisateur:
                menu_utilisateur(utilisateur)

        elif choix == "3":
            print("\n Enregistrement nouvel utilisateur")
            nom = input("Nom : ")
            prenom = input("Prénom : ")
            adresse = input("Adresse : ")
            phone = input("Téléphone : ")
            age = int(input("Âge : "))
            statut = input("Statut : ")
            idutilisateur = input("ID Utilisateur : ")
            login = input("Choisis un login : ")
            motdepasse = input("Choisis un mot de passe : ")

            util = Utilisateur(nom, prenom, adresse, phone, age, statut, idutilisateur, login, motdepasse)
            util.enregistrer_utilisateur()

        elif choix == "4":
            print("\n Enregistrement nouvel employé")
            nom = input("Nom : ")
            prenom = input("Prénom : ")
            adresse = input("Adresse : ")
            phone = input("Téléphone : ")
            age = int(input("Âge : "))
            statut = input("Statut : ")
            idemploye = input("ID Employé : ")
            shift = input("Shift : ")
            NAS = input("NAS : ")
            login = input("Choisis un login : ")
            motdepasse = input("Choisis un mot de passe : ")

            emp = Employe(nom, prenom, adresse, phone, age, statut, idemploye, shift, NAS, login, motdepasse)
            emp.enregistrer_employe()

        elif choix == "0":
            print(" Au revoir !")
            break
        else:
            print(" Choix invalide.")

def menu_employe(employe):
    while True:
        print(f"\n=== MENU EMPLOYÉ ({employe.nom}) ===")
        print("1. Ajouter un livre")
        print("2. Retirer un livre")
        print("3. Afficher la bibliothèque")
        print("4. Déconnexion")

        choix = input("Votre choix : ")

        if choix == "1":
            try:
                idlivre = int(input("ID livre : "))
                isbn = input("ISBN : ")
                titre = input("Titre : ")
                auteur = input("Auteur : ")
                annee = int(input("Année de publication : "))
                edition = input("Édition : ")
                from models.livre import Livre
                livre = Livre(idlivre, isbn, titre, auteur, annee, edition)
                employe.Ajouterlivre(livre)
            except ValueError:
                print(" Entrée invalide.")

        elif choix == "2":
            try:
                idlivre = int(input("ID du livre à retirer : "))
                employe.Retirerlivre(idlivre)
            except ValueError:
                print(" L'ID doit être un nombre entier.")

        elif choix == "3":
            employe.AfficherBibliotheque()

        elif choix == "4":
            print(" Déconnexion réussie.")
            break

        else:
            print(" Choix invalide.")

def menu_utilisateur(utilisateur):
    while True:
        print(f"\n=== MENU UTILISATEUR ({utilisateur.nom}) ===")
        print("1. Emprunter un livre")
        print("2. Retourner un livre")
        print("3. Voir les livres disponibles")
        print("4. Voir mon historique")
        print("5. Déconnexion")

        choix = input("Votre choix : ")

        if choix == "1":
            try:
                idlivre = int(input("ID du livre à emprunter : "))
                utilisateur.emprunter_livre(idlivre)
            except ValueError:
                print(" L'ID doit être un nombre entier.")

        elif choix == "2":
            try:
                idlivre = int(input("ID du livre à retourner : "))
                utilisateur.retourner_livre(idlivre)
            except ValueError:
                print(" L'ID doit être un nombre entier.")

        elif choix == "3":
            afficher_livres_disponibles()

        elif choix == "4":
            afficher_historique(utilisateur.idutilisateur)

        elif choix == "5":
            print(" Déconnexion réussie.")
            break

        else:
            print(" Choix invalide.")
