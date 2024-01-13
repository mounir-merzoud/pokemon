import pygame
import sys
import json

pygame.init()
largeur_fenetre = 800
hauteur_fenetre = 600
rouge = (255, 0, 0)
blanc = (255, 255, 255)
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Choix de Pokémon")

class GestionPokemon:
    def __init__(self, fichier_json):
        self.pokemon_data = self.charger_donnees(fichier_json)
        self.police = pygame.font.Font(None, 36)

    def charger_donnees(self, fichier_json):
        try:
            with open(fichier_json, 'r') as fichier:
                return json.load(fichier)
        except Exception as e:
            print(f"Une erreur s'est produite lors du chargement des données : {e}")
            return {}

    def afficher_pokemon(self):
        y_position = 50
        for nom, details in self.pokemon_data.items():
            texte_nom = self.police.render(f"Nom: {details['nom']}", True, blanc)
            fenetre.blit(texte_nom, (50, y_position))
            texte_niveau = self.police.render(f"Niveau: {details['niveau']}", True, blanc)
            fenetre.blit(texte_niveau, (50, y_position + 30))
            y_position += 80

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            fenetre.fill((0, 0, 0))  # Efface l'écran à chaque itération pour éviter le chevauchement du texte
            self.afficher_pokemon()
            pygame.display.flip()

if __name__ == "__main__":
    gestion_pokemon = GestionPokemon("donnees_pokemon.json")
    gestion_pokemon.run()
