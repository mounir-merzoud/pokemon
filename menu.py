import pygame
import sys

from choix_de_pokemon import *

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
largeur_fenetre = 800
hauteur_fenetre = 600

# Couleurs
rouge = (255, 0, 0)
blanc = (255, 255, 255)

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Menu Pokémon")

# Chargement de l'image de fond
image_fond = pygame.image.load("images/Pokemon-fond.png")
image_fond = pygame.transform.scale(image_fond, (largeur_fenetre, hauteur_fenetre))

# Paramètres des boutons
bouton_largeur = 300
bouton_hauteur = 50

# Font
police = pygame.font.Font(None, 36)
#gestion_pokemon = GestionPokemon("../donnees_pokemon.json")

# Fonction pour lancer une nouvelle partie
def nouvelle_partie():
    print("Lancer une nouvelle partie")
    from map import map # Importez la classe Map depuis votre fichier map.py
    nouvelle_partie_map = Map()  # Créez une nouvelle instance de Map
    nouvelle_partie_map.run() 
# Fonction pour choisir les Pokémon
def choisir_pokemon():
    print("Choisir Pokémon : Vous avez cliqué sur le bouton Choisir Pokémon")
    gestion_pokemon = GestionPokemon("donnees_pokemon.json")
    gestion_pokemon.run()
  
# Fonction pour accéder au Pokédex
def acceder_pokedex():
    print("Entrer sur le Pokédex")

# Fonction pour quitter la partie
def quitter_partie():
    pygame.quit()
    sys.exit()

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Gestion des clics de souris sur les boutons
            x, y = event.pos
            if 100 <= x <= 100 + bouton_largeur and 200 <= y <= 200 + bouton_hauteur:
                nouvelle_partie()
            elif 100 <= x <= 100 + bouton_largeur and 300 <= y <= 300 + bouton_hauteur:
                choisir_pokemon()
            elif 100 <= x <= 100 + bouton_largeur and 400 <= y <= 400 + bouton_hauteur:
                acceder_pokedex()
            elif 100 <= x <= 100 + bouton_largeur and 500 <= y <= 500 + bouton_hauteur:
                quitter_partie()

    # Affichage de l'image de fond
    fenetre.blit(image_fond, (0, 0))

    # Dessin des boutons
    pygame.draw.rect(fenetre, rouge, (100, 200, bouton_largeur, bouton_hauteur))  # Bouton nouvelle partie
    pygame.draw.rect(fenetre, rouge, (100, 300, bouton_largeur, bouton_hauteur))  # Bouton choisir Pokémon
    pygame.draw.rect(fenetre, rouge, (100, 400, bouton_largeur, bouton_hauteur))  # Bouton accéder au Pokédex
    pygame.draw.rect(fenetre, rouge, (100, 500, bouton_largeur, bouton_hauteur))  # Bouton quitter la partie

    # Ajout du texte
    texte_nouvelle_partie = police.render("Nouvelle Partie", True, blanc)
    fenetre.blit(texte_nouvelle_partie, (120, 215))

    texte_choisir_pokemon = police.render("Choisir Pokémon", True, blanc)
    fenetre.blit(texte_choisir_pokemon, (120, 315))

    texte_acceder_pokedex = police.render("Accéder au Pokédex", True, blanc)
    fenetre.blit(texte_acceder_pokedex, (120, 415))

    texte_quitter_partie = police.render("Quitter la partie", True, blanc)
    fenetre.blit(texte_quitter_partie, (120, 515))

    # Rafraîchissement de l'écran
    pygame.display.flip()

