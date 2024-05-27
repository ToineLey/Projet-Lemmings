from grille import Grille

class Direction:
    DROITE = 0
    GAUCHE = 1        


class Etats:
    STOP = 0
    MARCHER_1 = 1
    MARCHER_2 = 2
    MARCHER_3 = 3
    CREUSER_1 = 4
    CREUSER_2 = 5
    CHUTE = 6
    MORT = 7
    VICTOIRE = 8


class Lemming:
    def __init__(self, x, y):
        position_x = x
        position_y = y
        etat = Etats.MARCHER_1
        direction = Direction.DROITE
        arrive = False
        selectionne = False

    def changer_dir(self):
        self.direction = (self.direction + 1) % 2

    def deplacement(self, grille):
        if grille[self.y+1][self.x].est_libre():
            self.etat = Etats.CHUTE
            self.y -= 1
        elif self.direction() == 0 and grille[self.y][self.x+1].est_libre():
            self.etat = Etats.MARCHER_1 if self.etat == 6 or self.etat == 5 else self.etat + 1
            self.x += 1
        elif self.direction() == 1 and grille[self.y][self.x-1].est_libre():
            self.etat = Etats.MARCHER_1 if self.etat == 6 or self.etat == 5 else self.etat + 1
            self.x -= 1
        else:
            self.changer_dir()

    def arrivee(self):
        self.etat = Etats.VICTOIRE

    def creuse(self, grille):
        grille.creuser(self.x,self.y-1)
        self.etat = Etats.CREUSER_2 if self.etat == 1 else Etats.CREUSER_1

    def stop(self):
        self.etat = Etats.STOP

    def mort(self):
        self.etat = Etats.MORT

    def tour(self):
        # à compléter
        if 1 <= self.etat <= 6:
            self.deplacement()