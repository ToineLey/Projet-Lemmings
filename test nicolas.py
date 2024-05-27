import pyxel

class Jeu:
    def __init__(self):
        self.marche = [
            (0,0,0,16,16),
            (0,16,0,16,16),
            (0,32,0,16,16)
        ]
        self.creuse = [
            (0,0,32,16,16),
            (0,16,32,16,16)
        ]
        # taille de la fenetre 128x128 pixels
        # ne pas modifier
        pyxel.init(128, 128, title="lemmings", fps = 3)
        pyxel.load("lemmings.pyxres")
        pyxel.run(self.update, self.draw)

    # =====================================================
    # == UPDATE
    # =====================================================
    def update(self):
        """mise à jour des variables (30 fois par seconde)"""
        a = 1


    # =====================================================
    # == DRAW
    # =====================================================
    def draw(self):
        """création et positionnement des objets (30 fois par seconde)"""

        # vide la fenetre
        pyxel.cls(0)

        # vaisseau (carre 16x16)
        num_img = pyxel.frame_count % 3
        pyxel.blt(0,0,*self.marche[num_img])

        # creuser
        num_img = pyxel.frame_count % 2
        pyxel.blt(16,0, *self.creuse[num_img])

        # stop
        pyxel.blt(32,0,0,32,32,16,16)

        #bloc plein
        pyxel.blt(0,16,0,48,0,16,16)
Jeu()
           
