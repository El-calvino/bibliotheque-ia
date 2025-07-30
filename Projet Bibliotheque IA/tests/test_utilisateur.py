import unittest
from models.utilisateur import Utilisateur

class TestUtilisateur(unittest.TestCase):
    def test_creation_utilisateur(self):
        user = Utilisateur("Jean", "Dupont", "123 rue", "555-1234", 30, "Actif", "U001", "jdupont", "pass123")
        self.assertEqual(user.nom, "Jean")
        self.assertEqual(user.login, "jdupont")
