from grille import Grille

class Direction:
    DROITE = 0
    GAUCHE = 1

    def changer_dir(self):
        pass


class Etats:
    STOP = 0
    MARCHER_1 = 1
    MARCHER_2 = 2
    MARCHER_3 = 3
    CREUSER_1 = 4
    CREUSER_2 = 5
    CHUTE = 6
    MORT = 7


class Lemming:
    def __init__(self):
        position_x = int()
        position_y = int()
        etat = 'Etats.--'
        direction = 'Direction.--'
        arrive = bool()
        selectionne = bool()

    def deplacement(self):
        pass

    def arrivee(self):
        pass

    def creuse(self):
        pass

    def stop(self):
        pass

    def mort(self):
        pass

    def tour(self):
        pass