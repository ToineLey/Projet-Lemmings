class Type_t:
    AIR = 0
    TERRE_1 = 1
    TERRE_2 = 2
    TERRE_3 = 3
    TERRE_4 = 4
    TERRE_5 = 5
    VIDE = 6
    DEPART = 7
    ARRIVEE = 8


class Terrain:
    def __init__(self):
        position = tuple()
        terrain = 'Type_t.--'

    def est_libre(self):
        pass


class Grille:
    def __init__(self):
        map = list(list())
    
    def case(self, x, y):
        pass

    def creuser(self, x, y):
        pass

    def charger_grille(self):
        pass