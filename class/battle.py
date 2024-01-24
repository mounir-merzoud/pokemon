# battle.py
import pygame
import sys
from choix_de_pokemon import *


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

            # Charger les deux Pokémon (un sélectionné par l'utilisateur, l'autre choisi au hasard et différent)
            joueur, adversaire = self.gestion_pokemon.charger_pokemon_combat("donnees_pokemon.json")

            self.fenetre.fill((255, 255, 255))

            # Afficher le Pokémon sélectionné par l'utilisateur
            if joueur:
                nom_joueur = joueur['nom']
                niveau_joueur = joueur['niveau']
                font = pygame.font.Font(None, 24)
                texte_nom_joueur = font.render(f"Nom: {nom_joueur}", True, (0, 0, 0))
                texte_niveau_joueur = font.render(f"Niveau: {niveau_joueur}", True, (0, 0, 0))
                self.fenetre.blit(texte_nom_joueur, (20, 70))
                self.fenetre.blit(texte_niveau_joueur, (20, 100))

            # Afficher le Pokémon choisi au hasard et différent
            if adversaire:
                nom_adversaire = adversaire['nom']
                niveau_adversaire = adversaire['niveau']
                texte_nom_adversaire = font.render(f"Nom (Adversaire): {nom_adversaire}", True, (0, 0, 0))
                texte_niveau_adversaire = font.render(f"Niveau (Adversaire): {niveau_adversaire}", True, (0, 0, 0))
                self.fenetre.blit(texte_nom_adversaire, (400, 70))
                self.fenetre.blit(texte_niveau_adversaire, (400, 100))

            pygame.display.flip()

if __name__ == "__main__":
    battle_instance = Battle()
    battle_instance.run()

