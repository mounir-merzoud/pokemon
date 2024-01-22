# battle.py

import pygame
import sys
from choix_de_pokemon import GestionPokemon

pygame.init()

largeur_fenetre = 800
hauteur_fenetre = 600

fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Battle")

gestion_pokemon = GestionPokemon("donnees_pokemon.json", hauteur_fenetre)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i, (nom, details) in enumerate(list(gestion_pokemon.pokemon_data.items())[gestion_pokemon.scroll_offset:gestion_pokemon.scroll_offset + gestion_pokemon.lignes_visibles]):
                    y_position = gestion_pokemon.y_position + i * 80
                    bouton_rect = pygame.Rect(50, y_position + 10, 50, 50)
                    if bouton_rect.collidepoint(event.pos):
                        gestion_pokemon.select_pokemon(nom)

    # Charger le Pokémon sélectionné depuis le fichier JSON
    gestion_pokemon.charger_pokemon_selectionne("pokemon_selectionne.json")

    fenetre.fill((255, 255, 255))
    if gestion_pokemon.pokemon_selectionne:
        nom = gestion_pokemon.pokemon_selectionne['nom']
        niveau = gestion_pokemon.pokemon_selectionne['niveau']
        pygame.font.init()
        font = pygame.font.Font(None, 24)
        texte_nom = font.render(f"Nom: {nom}", True, (0, 0, 0))
        texte_niveau = font.render(f"Niveau: {niveau}", True, (0, 0, 0))
        fenetre.blit(texte_nom, (20, 70))
        fenetre.blit(texte_niveau, (20, 100))

    pygame.display.flip()
