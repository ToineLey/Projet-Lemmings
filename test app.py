from jeu import *
import pyxel as pyx

class App:
    def __init__(self,h,l):
        self.H,self.L = (h+1)*8,l*8
        self.y_interface=self.H-16
        pyx.init(self.L,self.H,title= 'Tst')
        self.x = 0
        self.apu=1
        self.bouton_1=True
        self.bouton_2=True
        self.bouton_3=True
        self.fc1=0
        self.fc2=0
        self.fc3=0
        self.b1,self.b2,self.b3=0,16,32
        pyx.load("lemmings.pyxres")
        # Lancement du jeu
        pyx.run(self.update, self.draw)
        
            
    def update(self):
        self.onclick()
        self.wait()

    def draw(self):
       pyx.cls(self.apu)
       self.bouton()
       pyx.mouse(True)

    def onclick(self):
        if pyx.btnp(pyx.MOUSE_BUTTON_LEFT,True,False):
            if pyx.mouse_x>=self.b1 and pyx.mouse_x<self.b1+16 and pyx.mouse_y>=self.y_interface and pyx.mouse_y<self.H:
                if self.bouton_1:
                    self.bouton_1=False
                    self.fc1=pyx.frame_count
            elif pyx.mouse_x>=self.b2 and pyx.mouse_x<self.b2+16 and pyx.mouse_y>=self.y_interface and pyx.mouse_y<self.H:
                if self.bouton_2:
                    self.bouton_2=False
                    self.fc2=pyx.frame_count
            elif pyx.mouse_x>=self.b3 and pyx.mouse_x<self.b3+16 and pyx.mouse_y>=self.y_interface and pyx.mouse_y<self.H:
                if self.bouton_3:
                    self.bouton_3=False
                    self.fc3=pyx.frame_count
        
    def wait(self):
        if pyx.frame_count==self.fc1+5:
            self.bouton_1=True
        if pyx.frame_count==self.fc2+5:
            self.bouton_2=True
        if pyx.frame_count==self.fc3+5:
            self.bouton_3=True
    
    def bouton(self):
        if self.bouton_1:
            pyx.blt(self.b1,self.y_interface,0,0,80,16,16)
        if self.bouton_2:
            pyx.blt(self.b2,self.y_interface,0,16,80,16,16)
        if self.bouton_3:
            pyx.blt(self.b3,self.y_interface,0,32,80,16,16)

App(16,32)






