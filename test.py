import pyxel as p

H,L = 6*8,8*8
t = [[None]*7 for _ in range(7)]

class Test:

    def __init__(self):
        p.init(H,L,title= 'Tst')
        self.x = 0
        p.load("my_resource.pyxres")
        # Lancement du jeu
        p.run(self.update, self.draw)
        
            
    def update(self):
       pass

    def draw(self):
       p.cls(0)


    def get_tilemap(self,t = [[]]):
        # parcourir une tilemap et recupérer les tuples en les metants dans un tableau de tableau de meme taille. 
        # Taille fixé à , 7.7 pour les testes.
        for i in range(8):
            for j in range(8):
                t[j][i] = p.tilemap(0).pget(j,i)
v = 0




Test()

					