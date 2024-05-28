from grille import Type_t,Terrain

class Grille:
    def __init__(self):
        map = [[Type_t.AIR,Type_t.AIR,Type_t.AIR]]
    
    def case(self, x, y):
        return self.map[x][y]

    def creuser(self, x, y):
        if self.case(x, y).terrain > 1:
            self.case(x, y).terrain -= 1
        else:
            self.map[x][y] = Terrain(x, y, Type_t.AIR)

    def charger_grille(self):
        pass