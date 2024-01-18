# choix_de_pokemon.py
import pygame
import json
import os
import sys

class GestionPokemon:
    def __init__(self, fichier_json):
        self.pokemon_data = self.charger_donnees(fichier_json)
        self.police = pygame.font.Font(None, 36)
        self.y_position = 50
        self.scroll_offset = 0
        self.lignes_visibles = int(hauteur_fenetre / 80)
        self.charger_images_pokemon()

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
                            # Ajoutez ici le code pour effectuer une action lorsque le bouton est cliqué.
                            # Par exemple, ouvrir une fenêtre d'informations sur le Pokémon.

    def run(self):
        while True:
            self.handle_events()
            fenetre.fill((0, 0, 0))
            self.afficher_boutons_pokemon(fenetre)
            pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    largeur_fenetre = 800
    hauteur_fenetre = 600
    blanc = (255, 255, 255)
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Choix de Pokémon")

    gestion_pokemon = GestionPokemon("donnees_pokemon.json")
    gestion_pokemon.run()
