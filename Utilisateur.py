
class Humain:
    def __init__(self, nom, prenom, adresse, phone, age, statut):
        self.nom = nom 
        self.prenom = prenom
        self.adresse = adresse
        self.phone = phone
        self.age = age
        self.statut = statut
        self.mot_de_passe = None  # mot de passe conservé sans propriété
        self.nom_utilisateur = None

    def afficher_infos(self):
        print("\n--- Informations de l'utilisateur ---")
        print(f"Nom : {self.nom}")
        print(f"Prénom : {self.prenom}")
        print(f"Adresse : {self.adresse}")
        print(f"Téléphone : {self.phone}")
        print(f"Âge : {self.age}")
        print(f"Statut : {self.statut}")

    def se_connecter(self, nom_utilisateur, mot_de_passe):
        self.nom_utilisateur = nom_utilisateur
        self.mot_de_passe = mot_de_passe
       
     


# --- Code d'exécution ---
print("--------- Bienvenue dans notre bibliothèque ---------")
nom = input("Quel est votre nom ? : ")
prenom = input("Quel est votre prénom ? : ")
adresse = input("Quelle est votre adresse ? : ")
phone = input("Quel est votre numéro de téléphone ? : ")
age = input("Quel est votre âge ? : ")
statut = input("Quel est votre statut (ex: Utilisateur ou Employé) ? : ")

utilisateur = Humain(nom, prenom, adresse, phone, age, statut)
utilisateur.afficher_infos()

print("------ Merci pour vos informations ! ------")
print("Passons à la connexion maintenant :")
nom_utilisateur = input("Veuillez saisir votre nom d'utilisateur : ")
mot_de_passe = input("Veuillez saisir votre mot de passe : ")

utilisateur.se_connecter(nom_utilisateur, mot_de_passe)

if utilisateur.mot_de_passe is not None:
    print("Connexion réussie !")
else:
    print("Échec de la connexion (mot de passe invalide).")
