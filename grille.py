

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
    def __init__(self,H,L):
        self.map = [[None]*(L//16) for _ in range(H//16)]
        
    
    def case(self, x, y):
        return self.map[y][x]

    def creuser(self, x, y):
        if self.case(x, y).terrain > 1:
            self.case(x, y).terrain -= 1
        else:
            self.map[y][x] = Terrain(x, y, Type_t.AIR)

# à modifier par Argan
    def charger_grille(self):
        """ parcourir une tilemap et recupérer les tuples en les metants dans un tableau de tableau de meme taille.
         Taille fixé à , 4.3 pour les testes ( voir le fichier Testtilmap.py)."""
        for i in range(self.len_x):
            for j in range(self.len_y):
                pass
                    #tab[i][j] = Dict_Test[pyx.tilemap(0).pget(i*2,j*2)]
    