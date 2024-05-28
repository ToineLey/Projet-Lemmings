from grille import Grille, Type_t

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
        self.case_x = x
        self.case_y = y
        self.dx = -1
        self.dy = -1
        self.etat = Etats.MARCHER_1
        self.direction = Direction.DROITE
        self.arrive = False
        self.selectionne = False

    def changer_dir(self):
        self.direction = (self.direction + 1) % 2

    def changer_etat_marche(self):
        if self.etat == Etats.MARCHER_1 or self.etat == Etats.MARCHER_2:
            self.etat += 1
        else:
            self.etat = Etats.MARCHER_1

    def chute(self):
        self.dy = self.dy + 1 if self.dy <= 7 else -8
        if self.dy == -8:
            self.case_y += 1

    def marche(self, pas):
        self.dx = self.dy + pas
        if self.dx < -8:
            self.case_x -= 1
            self.dx = 8
        elif self.dx > 8:
            self.case_x += 1
            self.dx = -8

    def deplacement(self, grille):
        if (self.dx == -1 or self.dx == 1) and grille.case(self.case_x, self.case_y+1).est_libre():
            self.etat = Etats.CHUTE

        if self.etat == Etats.CHUTE:
            if self.dy != -1:
                self.chute()
            else:
                if grille.case(self.case_x, self.case_y+1).est_libre():
                    self.chute()
                else:
                    self.changer_etat_marche()

        elif self.direction == Direction.DROITE:
            if self.dx != -1:
                self.marche(1)
            else:
                if grille.case(self.case_x+1, self.case_y).est_libre():
                    self.marche(1)
                else:
                    self.changer_dir()

        elif self.direction == Direction.GAUCHE:
            if self.dx != 1:
                self.marche(-1)
            else:
                if grille.case(self.case_x-1, self.case_y).est_libre():
                    self.marche(-1)
                else:
                    self.changer_dir()

    def arrivee(self):
        self.etat = Etats.VICTOIRE

    def creuse(self, grille):
        grille.creuser(self.x,self.y+1)
        self.etat = Etats.CREUSER_2 if self.etat == 1 else Etats.CREUSER_1

    def stop(self):
        self.etat = Etats.STOP