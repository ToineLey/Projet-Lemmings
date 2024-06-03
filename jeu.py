from niveau import *

class Timer:
    def __init__(self, n):
        self.niveau = n
        self.tps = int()

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
        self.charge_niveaux(H, L)
        self.timer = Timer(self.niveaux[0])

    def charge_niveaux(self, H, L):
        pass

    def fin_niveau(self):
        self.score += self.timer.niveau.calcul_score()
        try:
            self.timer = Timer(self.niveaux[self.timer.niveau.num_niveau + 1])
        except:
            self.fin = True