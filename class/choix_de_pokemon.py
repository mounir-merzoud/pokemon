# choix_de_pokemon.py

import pygame
import json
import os
import sys
from MENU import *

blanc = (255, 255, 255)

class GestionPokemon:
    def __init__(self, fichier_json, hauteur_fenetre):
        self.pokemon_data = self.charger_donnees(fichier_json)
        self.police = pygame.font.Font(None, 36)
        self.y_position = 50
        self.scroll_offset = 0
        self.lignes_visibles = int(hauteur_fenetre / 80)
        self.charger_images_pokemon()

        self.pokemon_selectionne = None
        self.nouveau_bouton_rect = pygame.Rect(600, 500, 150, 50)

    def charger_donnees(self, fichier_json):
        try:
            with open(fichier_json, 'r') as fichier:
                return json.load(fichier)
        except Exception as e:
            print(f"Une erreur s'est produite lors du chargement des données : {e}")
            return {}

    def charger_images_pokemon(self):
        self.images_pokemon = {}
        for nom, details in self.pokemon_data.items():
            chemin_image = os.path.join("images", details["images"])
            if os.path.exists(chemin_image):
                image = pygame.image.load(chemin_image)
                self.images_pokemon[nom] = pygame.transform.scale(image, (50, 50))

    def afficher_boutons_pokemon(self, surface):
        for i, (nom, details) in enumerate(list(self.pokemon_data.items())[self.scroll_offset:self.scroll_offset + self.lignes_visibles]):
            y_position = self.y_position + i * 80
            bouton_rect = pygame.Rect(50, y_position + 10, 50, 50)
            pygame.draw.rect(surface, blanc, bouton_rect, 2)

            texte_nom = self.police.render(f"Nom: {details['nom']}", True, blanc)
            surface.blit(texte_nom, (120, y_position))
            texte_niveau = self.police.render(f"Niveau: {details['niveau']}", True, blanc)
            surface.blit(texte_niveau, (120, y_position + 30))

            if nom in self.images_pokemon:
                surface.blit(self.images_pokemon[nom], (50, y_position + 10))

        pygame.draw.rect(surface, blanc, self.nouveau_bouton_rect, 2)
        texte_nouveau_bouton = self.police.render("back", True, blanc)
        surface.blit(texte_nouveau_bouton, (self.nouveau_bouton_rect.x + 10, self.nouveau_bouton_rect.y + 10))

    def select_pokemon(self, nom):
        print(f"Pokémon sélectionné : {nom}")
        self.pokemon_selectionne = self.pokemon_data.get(nom)

    def sauvegarder_pokemon_selectionne(self, fichier_json):
        if self.pokemon_selectionne:
            with open(fichier_json, 'w') as fichier:
                json.dump({"selected_pokemon": self.pokemon_selectionne}, fichier)

    def charger_pokemon_selectionne(self, fichier_json):
        try:
            with open(fichier_json, 'r') as fichier:
                data = json.load(fichier)
                self.pokemon_selectionne = data.get("selected_pokemon")
        except Exception as e:
            print(f"Une erreur s'est produite lors du chargement du Pokémon sélectionné : {e}")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Scroll up
                    self.scroll_offset = max(0, self.scroll_offset - 1)
                elif event.button == 5:  # Scroll down
                    self.scroll_offset = min(len(self.pokemon_data) - self.lignes_visibles, self.scroll_offset + 1)
                elif event.button == 1:  # Left click
                    for i, (nom, details) in enumerate(list(self.pokemon_data.items())[self.scroll_offset:self.scroll_offset + self.lignes_visibles]):
                        y_position = self.y_position + i * 80
                        bouton_rect = pygame.Rect(50, y_position + 10, 50, 50)
                        if bouton_rect.collidepoint(event.pos):
                            print(f"Bouton {nom} cliqué!")
                            self.select_pokemon(nom)
                    if self.nouveau_bouton_rect.collidepoint(event.pos):
                        self.sauvegarder_pokemon_selectionne("pokemon_selectionne.json")
                        menu = Menu()
                        menu.run()
                        self.nouveau_bouton_clic()

    def nouveau_bouton_clic(self):
        print("Nouveau bouton cliqué!")
        if self.pokemon_selectionne:
            print("Informations du Pokémon sélectionné:")
            print(f"Nom: {self.pokemon_selectionne['nom']}")
            print(f"Niveau: {self.pokemon_selectionne['niveau']}")

    def run(self, fenetre):
        while True:
            self.handle_events()
            fenetre.fill((0, 0, 0))
            self.afficher_boutons_pokemon(fenetre)
            pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    largeur_fenetre = 800
    hauteur_fenetre = 620
    blanc = (255, 255, 255)
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Choix de Pokémon")

    gestion_pokemon = GestionPokemon("donnees_pokemon.json", hauteur_fenetre)
    gestion_pokemon.run(fenetre)
    pygame.quit()
    sys.exit()
