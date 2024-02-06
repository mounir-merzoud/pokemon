
import pygame

class BarreDeVie:
    def __init__(self, x, y, couleur):
        self.x = x
        self.y = y
        self.longueur_barre = 200
        self.largeur_barre = 20
        self.font = pygame.font.Font(None, 20)
        self.vie = 100  # Défaut de vie à 100
        self.couleur = couleur  # Couleur de la barre de vie

    def afficher(self, surface, vie):
        vie_max = 100
        longueur_vie = int(self.longueur_barre * vie / vie_max)
        pygame.draw.rect(surface, (0, 0, 0), (self.x, self.y, self.longueur_barre, self.largeur_barre), 2)
        if vie > 0:
            pygame.draw.rect(surface, self.couleur, (self.x, self.y, longueur_vie, self.largeur_barre))
            texte_vie = self.font.render(str(vie), True, (0, 0, 0))
            surface.blit(texte_vie, (self.x + self.longueur_barre + 10, self.y))

    def update_vie(self, vie):
        self.vie = vie  # Met à jour la vie
