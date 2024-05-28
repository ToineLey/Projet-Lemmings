from jeu import *
import pyxel as pyx

H,L = 6*8,8*8
t = [[None]*3 for _ in range(4)]

class App:
    def __init__(self,longeur_x,longeur_y):
        self.len_x = longeur_x
        self.len_y = longeur_y
        pyx.init(H,L,title= 'Tst')
        self.x = 0
        self.apu=0
        self.t=True
        self.t2=True
        pyx.load("bouton.pyxres")
        self.get_tilemap(t)
        # Lancement du jeu
        pyx.run(self.update, self.draw)
        
            
    def update(self):
        self.onclick()

    def draw(self):
       pyx.cls(self.apu)
       self.bouton()
       pyx.mouse(True)

    def onclick(self):
        if pyx.btnp(pyx.MOUSE_BUTTON_LEFT,True,False):
            if pyx.mouse_x>=0 and pyx.mouse_x<16 and pyx.mouse_y>=0 and pyx.mouse_y<16:
                if self.t:
                    self.t=False
                elif not self.t:
                    self.t=True
            elif pyx.mouse_x>=16 and pyx.mouse_x<32 and pyx.mouse_y>=16 and pyx.mouse_y<32:
                if self.t2:
                    self.t2=False
                elif not self.t2:
                    self.t2=True
            else:
                if self.apu==15:
                    self.apu=0
                else:
                    self.apu+=1
        
    def bouton(self):
        if self.t:
            pyx.blt(0,0,0,0,0,16,16)
        if self.t2:
            pyx.blt(16,16,0,16,0,16,16)

    def get_tilemap(self,tab):
        # parcourir une tilemap et recupérer les tuples en les metants dans un tableau de tableau de meme taille. 
        # Taille fixé à , 7.7 pour les testes.
        for i in range(self.len_y):
            for j in range(self.len_x):
                tab[i][j] = pyx.tilemap(0).pget(i*2,j*2)

App(3,4)