from lemming import *
from grille import Grille
import pyxel as pyx
import json




class Niveau:
    def __init__(self,num_niv):
        self.num_niveau = num_niv # correspond u niveau de la tilmap
        grille = 'Grille()'
        taille_gr = ()
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

    """def charger_nv(self):
        for i in range(self.len_x):
            for j in range(self.len_y):
                    tab[i][j] = Dict_Test[pyx.tilemap(0).pget(i*2,j*2)]"""
    
    def charger_json(self):

        if self.num_niv < 1:
            return ValueError
        else:
            with open('niveaux.json') as file:
                tab_json = json.load(file)

