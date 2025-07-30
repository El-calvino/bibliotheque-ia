from models.livre import Livre

# Création d'un livre
livre = Livre(1, "123456789", "Le Petit Prince", "Antoine de Saint-Exupéry", 1943, "1ère")

# Affichage des attributs
print("Titre :", livre.titre)
print("Auteur :", livre.auteur)
print("Disponible :", livre.disponible)

# Vérification du dictionnaire
print("Dictionnaire :", livre.to_dict())
