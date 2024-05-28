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
    def __init__(self, x, y, type):
        position = (x, y)
        terrain = type

    def est_libre(self):
        return not 1 <= self.terrain < 6


class Grille:
    def __init__(self):
        map = list(list())
    
    def case(self, x, y):
        return self.map[x][y]

    def creuser(self, x, y):
        if self.case(x, y).terrain > 1:
            self.case(x, y).terrain -= 1
        else:
            self.map[x][y] = Terrain(x, y, Type_t.AIR)

# à modifier par Argan
    def charger_grille(self):
        pass