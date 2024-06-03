from jeu import *
import pyxel as pyx
import time

H,L = 17*8,32*8
y_interface=H-16
t = [[None]*3 for _ in range(4)]

class App:
    def __init__(self,longeur_x,longeur_y):
        self.len_x = longeur_x
        self.len_y = longeur_y
        pyx.init(L,H,title= 'Tst')
        self.x = 0
        self.apu=1
        self.t=True
        self.t2=True
        self.t3=True
        self.b1,self.b2,self.b3=0,16,32
        pyx.load("lemmings.pyxres")
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
            if pyx.mouse_x>=self.b1 and pyx.mouse_x<self.b1+16 and pyx.mouse_y>=y_interface and pyx.mouse_y<H:
                if self.t:
                    self.t=False
                elif not self.t:
                    self.t=True
            elif pyx.mouse_x>=self.b2 and pyx.mouse_x<self.b2+16 and pyx.mouse_y>=y_interface and pyx.mouse_y<H:
                if self.t2:
                    self.t2=False
                elif not self.t2:
                    self.t2=True
            elif pyx.mouse_x>=self.b3 and pyx.mouse_x<self.b3+16 and pyx.mouse_y>=y_interface and pyx.mouse_y<H:
                if self.t3:
                    self.t3=False
                elif not self.t3:
                    self.t3=True
        
    def bouton(self):
        if self.t:
            pyx.blt(self.b1,y_interface,0,0,80,16,16)
        if self.t2:
            pyx.blt(self.b2,y_interface,0,16,80,16,16)
        if self.t3:
            pyx.blt(self.b3,y_interface,0,32,80,16,16)

    def get_tilemap(self,tab):
        # parcourir une tilemap et recupérer les tuples en les metants dans un tableau de tableau de meme taille. 
        # Taille fixé à , 7.7 pour les testes.
        for i in range(self.len_y):
            for j in range(self.len_x):
                tab[i][j] = pyx.tilemap(0).pget(i*2,j*2)

App(3,4)