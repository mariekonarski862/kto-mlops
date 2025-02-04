import unittest

"""
Count names with more than seven letters
"""
def names(prenoms):
    more_than_seven = 0
    for prenom in prenoms:
        if len(prenom) > 7:
            more_than_seven += 1
            print(prenom + " est un prénom avec un nombre de lettres supérieur à 7")
        else:
            print(prenom + " est un prénom avec un nombre de lettres inférieur ou égal à 7")
    return more_than_seven

class TestNamesMethod(unittest.TestCase):
     def test_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seven = names(prenoms=prenoms)
        self.assertEqual(more_than_seven, 4)

if __name__ == '__main__':
    unittest.main()

#version corrigée
import unittest

seuil_mot_long = 7
#Compte le nombre de prénoms considéré comme long (si plus de 7 lettres)

def compter_prenoms_long (prenoms: list[str]) -> int:
    nombre_prenom_long = 0
    for prenom in prenoms:
        if len(prenom) > seuil_mot_long:
            nombre_prenom_long += 1
            print(prenom + " est un prénom long")
        else:
            print(prenom + " est un prénom court")
    return nombre_prenom_long

class Testcompter_nombre_prenoms_long_Method(unittest.TestCase):
     def test_compter_prenoms_long(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        nombre_prenom_long = compter_prenoms_long(prenoms=prenoms)
        self.assertEqual(nombre_prenom_long, 4)

if __name__ == '__main__':
    unittest.main()
