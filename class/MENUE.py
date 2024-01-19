import pygame
import sys
from map import * 
# Assurez-vous également d'importer les autres classes nécessaires (GestionPokemon, etc.) si elles ne sont pas déjà importées

pygame.init()

# Définir la taille de la fenêtre
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

# Charger l'image de fond
bg = pygame.image.load("images/background.png")

# Définir la police
font = pygame.font.Font(None, 36)

# Définir les couleurs
white = (255, 255, 255)
black = (0, 0, 0)

# Définir les textes
text_nouvelle_partie = font.render("Nouvelle Partie", True, black)
text_choisir_pokemon = font.render("Choisir Pokémon", True, black)
text_acceder_pokedex = font.render("Accéder au Pokédex", True, black)
text_quitter_partie = font.render("Quitter la Partie", True, black)

def nouvelle_partie():
    print("Lancer une nouvelle partie")

def choisir_pokemon():
    print("Choisir Pokémon : Vous avez cliqué sur le bouton Choisir Pokémon")
    # Ajoutez le code nécessaire pour gérer le choix du Pokémon

def acceder_pokedex():
    print("Entrer sur le Pokédex")
    # Ajoutez le code nécessaire pour accéder au Pokédex

def quitter_partie():
    pygame.quit()
    sys.exit()

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitter_partie()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if text_nouvelle_partie.get_rect().collidepoint(pygame.mouse.get_pos()):
                nouvelle_partie()
            elif text_choisir_pokemon.get_rect().collidepoint(pygame.mouse.get_pos()):
                choisir_pokemon()
            elif text_acceder_pokedex.get_rect().collidepoint(pygame.mouse.get_pos()):
                acceder_pokedex()
            elif text_quitter_partie.get_rect().collidepoint(pygame.mouse.get_pos()):
                quitter_partie()

    # Afficher l'arrière-plan
    screen.blit(bg, (0, 0))

    # Afficher les textes
    screen.blit(text_nouvelle_partie, (50, 50))
    screen.blit(text_choisir_pokemon, (50, 100))
    screen.blit(text_acceder_pokedex, (50, 150))
    screen.blit(text_quitter_partie, (50, 200))

    pygame.display.flip()
