# battle.py
import pygame
import sys
from choix_de_pokemon import GestionPokemon

class Battle:
    def __init__(self):
        pygame.init()

        self.largeur_fenetre = 800
        self.hauteur_fenetre = 600

        self.fenetre = pygame.display.set_mode((self.largeur_fenetre, self.hauteur_fenetre))
        pygame.display.set_caption("Battle")

        self.gestion_pokemon = GestionPokemon("donnees_pokemon.json", self.hauteur_fenetre)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for i, (nom, details) in enumerate(list(self.gestion_pokemon.pokemon_data.items())[self.gestion_pokemon.scroll_offset:self.gestion_pokemon.scroll_offset + self.gestion_pokemon.lignes_visibles]):
                            y_position = self.gestion_pokemon.y_position + i * 80
                            bouton_rect = pygame.Rect(50, y_position + 10, 50, 50)
                            if bouton_rect.collidepoint(event.pos):
                                self.gestion_pokemon.select_pokemon(nom)

            # Charger le Pokémon sélectionné depuis le fichier JSON
            self.gestion_pokemon.charger_pokemon_selectionne("pokemon_selectionne.json")

            self.fenetre.fill((255, 255, 255))
            if self.gestion_pokemon.pokemon_selectionne:
                nom = self.gestion_pokemon.pokemon_selectionne['nom']
                niveau = self.gestion_pokemon.pokemon_selectionne['niveau']
                pygame.font.init()
                font = pygame.font.Font(None, 24)
                texte_nom = font.render(f"Nom: {nom}", True, (0, 0, 0))
                texte_niveau = font.render(f"Niveau: {niveau}", True, (0, 0, 0))
                self.fenetre.blit(texte_nom, (20, 70))
                self.fenetre.blit(texte_niveau, (20, 100))

            pygame.display.flip()

if __name__ == "__main__":
    battle_instance = Battle()
    battle_instance.run()
