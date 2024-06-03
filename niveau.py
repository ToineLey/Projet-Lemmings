from lemming import *
from grille import Grille

class Niveau:
    def __init__(self, grille, n:int):
        self.nb_niveau = n # correspond au niveau de la tilmap
        self.grille = grille
        self.nb_lem_dep = int()
        self.nb_lem_arr = int()
        self.coo_dep = tuple()
        self.coo_arr = tuple()
        self.lem_IGM = set()

    def apparition(self):
        self.lem_IGM.add(Lemming(*self.coo_dep))

    def calcul_score(self):
        return (self.nb_lem_arr/self.nb_lem_dep) * 100

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
        elif lem.etat == Etats.STOP:
            lem.dx, lem.dy = 0, 0
            self.grille.case(lem.x, lem.y).terrain = Type_t.TERRE_1
