class Livre:
    def __init__(self, idlivre, ISBN, titre, auteur, anneepublication, edition, disponible=True):
        self.idlivre = idlivre
        self.ISBN = ISBN
        self.titre = titre
        self.auteur = auteur
        self.anneepublication = anneepublication
        self.edition = edition
        self.disponible = disponible

    def to_dict(self):
        return {
            "idlivre": self.idlivre,
            "ISBN": self.ISBN,
            "titre": self.titre,
            "auteur": self.auteur,
            "anneepublication": self.anneepublication,
            "edition": self.edition,
            "disponible": self.disponible
        }
    



