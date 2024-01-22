import pygame
import sys
import random
import os
from choix_de_pokemon import *
class mon_pokemon:
    

pygame.init()

largeur_fenetre = 800
hauteur_fenetre = 620
blanc = (255, 255, 255)
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Combat")
fenetre.fill(blanc)
# Ajoutez ici le reste de votre code pour le traitement du combat

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ajoutez ici le reste de votre code pour le traitement du combat

    # Mettez à jour l'affichage
    pygame.display.flip()

# Quitter pygame et le script
pygame.quit()
sys.exit()

