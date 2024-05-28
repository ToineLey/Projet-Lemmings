import pyxel as pyx
from grille import Type_t

H,L = 6*8,8*8
t = [[None]*3 for _ in range(4)]

### Dictionnaire du terrain, avec tous les terrains possibles dans la nivaux ###
Dict_Terrain = {
    (2,4) : Type_t.AIR,
    (4,4) : Type_t.TERRE_1,
    (0,6) : Type_t.TERRE_2,
    (2,6) : Type_t.TERRE_3,
    (4,6) : Type_t.TERRE_4,
    (6,6) : Type_t.TERRE_5,
    (0,4) : Type_t.VIDE,
    (0,8) : Type_t.DEPART,
    (2,8) : Type_t.ARRIVEE
}


class Test:

    def __init__(self,longeur_x,longeur_y):
        self.len_x = longeur_x
        self.len_y = longeur_y
        pyx.init(H,L,title= 'Tst')
        self.x = 0
        pyx.load("Test.pyxres")
        self.get_tilemap(t)
        print(t)
        # Lancement du jeu
        pyx.run(self.update, self.draw)
        
            
    def update(self):
        a = 1

    def draw(self):
       pyx.cls(0)



    def get_tilemap(self,tab):
        # parcourir une tilemap et recupérer les tuples en les metants dans un tableau de tableau de meme taille. 
        # Taille fixé à , 7.7 pour les testes.
        for i in range(self.len_y):
            for j in range(self.len_x):
                tab[i][j] = pyx.tilemap(0).pget(i*2,j*2)
        
    
def affiche_tuples(tab,x,y):
    return tab[x][y]




Test(3,4)

					