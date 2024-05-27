from lemming import *
from grille import Grille

class Niveau:
    def __init__(self):
        nb_niveau = int()
        grille = 'Grille()'
        nb_lem_dep = int()
        nb_lem_arr = int()
        coo_dep = tuple()
        coo_arr = tuple()
        lem_IGM = set()

    def apparition(self):
        self.lem_IGM.add(Lemming(*self.coo_dep))

    def calcul_score(self):
        pass