from lemming import *
from grille import Grille

class Niveau:
    def __init__(self):
        nb_niveau = int() # correspond u niveau de la tilmap
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

    def tour_lemmings(self, lem):
        # à compléter
        if self.grille.case(lem.x, lem.y).terrain == Type_t.VIDE:
            lem.etat = Etats.MORT
        elif tuple(lem.x, lem.y) == self.coo_arr:
            lem.etat = Etats.VICTOIRE
        if Etats.MARCHER_1 <= lem.etat <= Etats.MARCHER_3 or lem.etat == Etats.CHUTE:
            lem.deplacement(self.grille)
        elif lem.etat == Etats.CREUSER_1 or lem.etat == Etats.CREUSER_2:
            lem.creuse(self.grille)