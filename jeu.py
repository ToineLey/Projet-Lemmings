from niveau import *

class Timer:
    def __init__(self, t):
        self.tps = t
        self.niveau = Niveau()

    def rebour(self):
        self.tps -= 1

    def tour(self):
        for lemming in self.niveau.lem_IGM:
            self.niveau.tour_lemmings(lemming)


class Jeu:
    def __init__(self, H, L):
        self.fin = False
        self.score = 0
        self.niveaux = None
        self.timer = None
        self.charge_niveaux(H, L)

    def charge_niveaux(self, H, L):
        pass

    def fin_partie(self):
        pass

    def fin_niveau(self):
        pass

    def debut_niveau(self):
        pass