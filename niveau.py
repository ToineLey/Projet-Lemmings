from lemming import *
from grille import Grille,Type_t
import pyxel as pyx
import json

Dict_Terrain = {
    (2,4) : Type_t.AIR,
    (4,4) : Type_t.TERRE_1,
    (6,4) : Type_t.TERRE_1,
    (0,6) : Type_t.TERRE_2,
    (2,6) : Type_t.TERRE_3,
    (4,6) : Type_t.TERRE_4,
    (6,6) : Type_t.TERRE_5,
    (0,4) : Type_t.VIDE,
    (0,8) : Type_t.DEPART,
    (2,8) : Type_t.ARRIVEE
}


class Niveau:
    def __init__(self, n:int,H,L):
        self.num = n - 1 # correspond au niveau de la tilmap
        self.nom = ""
        self.grille = Grille(H,L)
        self.nb_lem_dep = int()
        self.nb_lem_arr = int()
        self.coo_dep = tuple()
        self.coo_arr = tuple()
        self.lem_IGM = set()
        self.charger_nv(H,L)



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

    def charger_nv(self,H,L):
        for i in range(L):
            for j in range(H):
                    self.grille.map[i][j] = Dict_Terrain[pyx.tilemap(self.num).pget(i*2,j*2)]
    
    def charger_json(self):
        if self.num < 0:
            return ValueError
        else:
            with open('niveaux.json') as file:
                tab_json = json.load(file)
            self.nom = tab_json[self.num]['nom']
            self.nb_lem_dep = tab_json[self.num]['nb_lemmings_dep']


