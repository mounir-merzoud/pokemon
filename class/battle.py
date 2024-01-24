import pygame
import sys
import json
from choix_de_pokemon import *

class Battle:
    def __init__(self):
        pygame.init()

        self.largeur_fenetre = 800
        self.hauteur_fenetre = 600

        self.fenetre = pygame.display.set_mode((self.largeur_fenetre, self.hauteur_fenetre))
        pygame.display.set_caption("Battle")

        self.gestion_pokemon = GestionPokemon("donnees_pokemon.json", self.hauteur_fenetre)

        # Initialise la police
        self.font = pygame.font.Font(None, 24)

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

            joueur, adversaire = self.gestion_pokemon.charger_pokemon_combat("donnees_pokemon.json")

            self.fenetre.fill((255, 255, 255))

            if joueur:
                nom_joueur = joueur['nom']
                niveau_joueur = joueur['niveau']
                chemin_image_joueur = f"C:\\Users\\lo\\Desktop\\bbt\\PYTHON\\P_O_O\\pokemon\\images\\{joueur['images']}"
                type_dattaque_joueur = joueur['type_dattaque']
                point_de_vie_joueur = joueur['point_de_vie']
                puissance_dattaque_joueur = joueur['puissance_dattaque']
                defense_joueur = joueur['defense']

                texte_nom_joueur = self.font.render(f"Nom: {nom_joueur}", True, (0, 0, 0))
                texte_niveau_joueur = self.font.render(f"Niveau: {niveau_joueur}", True, (0, 0, 0))
                texte_type_dattaque_joueur = self.font.render(f"Type d'attaque: {type_dattaque_joueur}", True, (0, 0, 0))
                texte_point_de_vie_joueur = self.font.render(f"Point de vie: {point_de_vie_joueur}", True, (0, 0, 0))
                texte_puissance_dattaque_joueur = self.font.render(f"Puissance d'attaque: {puissance_dattaque_joueur}", True, (0, 0, 0))
                texte_defense_joueur = self.font.render(f"Défense: {defense_joueur}", True, (0, 0, 0))

                self.fenetre.blit(texte_nom_joueur, (20, 70))
                self.fenetre.blit(texte_niveau_joueur, (20, 100))
                self.fenetre.blit(texte_type_dattaque_joueur, (20, 130))
                self.fenetre.blit(texte_point_de_vie_joueur, (20, 160))
                self.fenetre.blit(texte_puissance_dattaque_joueur, (20, 190))
                self.fenetre.blit(texte_defense_joueur, (20, 220))

                # Enregistrement du Pokémon sélectionné dans un fichier JSON externe
                pokemon_selectionne = {
                    "nom": nom_joueur,
                    "niveau": niveau_joueur,
                    "chemin_image": chemin_image_joueur,
                    "type_dattaque": type_dattaque_joueur,
                    "point_de_vie": point_de_vie_joueur,
                    "puissance_dattaque": puissance_dattaque_joueur,
                    "defense": defense_joueur
                }
                with open("../pokemon_selectionne.json", "w") as json_file:
                    json.dump(pokemon_selectionne, json_file)

                # Charger et afficher l'image du joueur sélectionné
                image_joueur = pygame.image.load(chemin_image_joueur)
                image_joueur = pygame.transform.scale(image_joueur, (100, 100))  # Ajustez la taille selon vos besoins
                self.fenetre.blit(image_joueur, (150, 70))

            if adversaire:
                nom_adversaire = adversaire['nom']
                niveau_adversaire = adversaire['niveau']
                chemin_image_adversaire = f"C:\\Users\\lo\\Desktop\\bbt\\PYTHON\\P_O_O\\pokemon\\images\\{adversaire['images']}" # Assurez-vous d'ajouter cette ligne si les données de votre adversaire incluent le chemin de l'image
                texte_nom_adversaire = self.font.render(f"Nom (Adversaire): {nom_adversaire}", True, (0, 0, 0))
                texte_niveau_adversaire = self.font.render(f"Niveau (Adversaire): {niveau_adversaire}", True, (0, 0, 0))
                self.fenetre.blit(texte_nom_adversaire, (400, 70))
                self.fenetre.blit(texte_niveau_adversaire, (400, 100))

                # Charger et afficher l'image de l'adversaire
                image_adversaire = pygame.image.load(chemin_image_adversaire)
                image_adversaire = pygame.transform.scale(image_adversaire, (100, 100))  # Ajustez la taille selon vos besoins
                self.fenetre.blit(image_adversaire, (550, 70))

            pygame.display.flip()

if __name__ == "__main__":
    battle_instance = Battle()
    battle_instance.run()

