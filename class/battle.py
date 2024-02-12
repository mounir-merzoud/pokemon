import pygame
import sys
from choix_de_pokemon import GestionPokemon
from barre_de_vie import *

class Battle:
    def __init__(self):
        pygame.init()

        self.largeur_fenetre = 800
        self.hauteur_fenetre = 600

        self.fenetre = pygame.display.set_mode((self.largeur_fenetre, self.hauteur_fenetre))
        pygame.display.set_caption("Battle")

        self.gestion_pokemon = GestionPokemon("donnees_pokemon.json", self.hauteur_fenetre)

        self.font = pygame.font.Font(None, 24)

        self.pokemon1_attaque = False
        self.pokemon2_attaque = False

        self.pokemon1 = None
        self.pokemon2 = None

        self.barre_vie_pokemon1 = BarreDeVie(20, 160, (0, 255, 0))  # Couleur verte pour le Pokémon 1
        self.barre_vie_pokemon2 = BarreDeVie(400, 160, (255, 0, 0))  # Couleur rouge pour le Pokémon 2

    def attaquer(self, attaquant, cible):
        degat = self.calculate_damage(attaquant, cible)
        print(f"Dégâts infligés : {degat}")
        self.apply_damage(cible, degat)
        print(f"Points de vie de {cible['nom']} après attaque : {cible['point_de_vie']}")

    def apply_damage(self, pokemon, damage):
        print(f"Avant l'attaque - Points de vie de {pokemon['nom']} : {pokemon['point_de_vie']}")
        pokemon["point_de_vie"] -= damage
        print(f"Après l'attaque - Points de vie de {pokemon['nom']} : {pokemon['point_de_vie']}")

    def calculate_damage(self, attaquant, cible):
        if attaquant['type_dattaque'] == "eau":
            degat = 15
        elif attaquant['type_dattaque'] == "terre":
            degat = 10
        elif attaquant['type_dattaque'] == "feu":
            degat = 20
        elif attaquant['type_dattaque'] == "normal":
            degat = 5
        return degat

    def determiner_gagnant(self):
        if self.pokemon1['point_de_vie'] <= 0 and self.pokemon2['point_de_vie'] > 0:
            return self.pokemon2['nom']
        elif self.pokemon2['point_de_vie'] <= 0 and self.pokemon1['point_de_vie'] > 0:
            return self.pokemon1['nom']
        else:
            return "Match nul"

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:  # Touche gauche du clavier
                        self.pokemon2_attaque = True
                        self.pokemon1_attaque = False
                    elif event.key == pygame.K_RIGHT:  # Touche droite du clavier
                        self.pokemon1_attaque = True
                        self.pokemon2_attaque = False

            pokemon1, pokemon2 = self.gestion_pokemon.charger_pokemon_combat("donnees_pokemon.json")

            self.fenetre.fill((255, 255, 255))

            if pokemon1:
                self.pokemon1 = pokemon1
                self.barre_vie_pokemon1.update_vie(pokemon1['point_de_vie'])  # Met à jour la vie du Pokémon 1
                self.barre_vie_pokemon1.afficher(self.fenetre, pokemon1['point_de_vie'])

                nom_pokemon1 = pokemon1['nom']
                niveau_pokemon1 = pokemon1['niveau']
                chemin_image_pokemon1 = f"images/{pokemon1['images']}"
                type_dattaque_pokemon1 = pokemon1['type_dattaque']

                texte_nom_pokemon1 = self.font.render(f"Nom: {nom_pokemon1}", True, (0, 0, 0))
                texte_niveau_pokemon1 = self.font.render(f"Niveau: {niveau_pokemon1}", True, (0, 0, 0))
                texte_type_dattaque_pokemon1 = self.font.render(f"Type d'attaque: {type_dattaque_pokemon1}", True,
                                                                 (0, 0, 0))

                self.fenetre.blit(texte_nom_pokemon1, (20, 70))
                self.fenetre.blit(texte_niveau_pokemon1, (20, 100))
                self.fenetre.blit(texte_type_dattaque_pokemon1, (20, 130))

                image_pokemon1 = pygame.image.load(chemin_image_pokemon1)
                image_pokemon1 = pygame.transform.scale(image_pokemon1, (100, 100))
                self.fenetre.blit(image_pokemon1, (150, 350))

            if pokemon2:
                self.pokemon2 = pokemon2
                self.barre_vie_pokemon2.update_vie(pokemon2['point_de_vie'])  # Met à jour la vie du Pokémon 2
                self.barre_vie_pokemon2.afficher(self.fenetre, pokemon2['point_de_vie'])

                nom_pokemon2 = pokemon2['nom']
                niveau_pokemon2 = pokemon2['niveau']
                chemin_image_pokemon2 = f"images/{pokemon2['images']}"
                type_dattaque_pokemon2 = pokemon2['type_dattaque']

                texte_nom_pokemon2 = self.font.render(f"Nom: {nom_pokemon2}", True, (0, 0, 0))
                texte_niveau_pokemon2 = self.font.render(f"Niveau: {niveau_pokemon2}", True, (0, 0, 0))
                texte_type_dattaque_pokemon2 = self.font.render(f"Type d'attaque: {type_dattaque_pokemon2}", True,
                                                                 (0, 0, 0))

                self.fenetre.blit(texte_nom_pokemon2, (400, 70))
                self.fenetre.blit(texte_niveau_pokemon2, (400, 100))
                self.fenetre.blit(texte_type_dattaque_pokemon2, (400, 130))

                image_pokemon2 = pygame.image.load(chemin_image_pokemon2)
                image_pokemon2 = pygame.transform.scale(image_pokemon2, (100, 100))
                self.fenetre.blit(image_pokemon2, (550, 350))

            if self.pokemon2_attaque and self.pokemon1:
                print(f"{self.pokemon2['nom']} attaque avec {self.pokemon2['type_dattaque']} ")
                degat = self.calculate_damage(self.pokemon2, self.pokemon1)
                self.apply_damage(self.pokemon1, degat)
                if self.pokemon1:  # Vérification que pokemon1 est initialisé
                    self.barre_vie_pokemon1.update_vie(self.pokemon1['point_de_vie'])
                    self.barre_vie_pokemon1.afficher(self.fenetre, self.pokemon1['point_de_vie'])  # Affichage mis à jour
                self.pokemon2_attaque = False

            if self.pokemon1_attaque and self.pokemon2:
                print(f"{self.pokemon1['nom']} attaque avec {self.pokemon1['type_dattaque']} !")
                degat = self.calculate_damage(self.pokemon1, self.pokemon2)
                self.apply_damage(self.pokemon2, degat)
                if self.pokemon2:  # Vérification que pokemon2 est initialisé
                    self.barre_vie_pokemon2.update_vie(self.pokemon2['point_de_vie'])
                    self.barre_vie_pokemon2.afficher(self.fenetre, self.pokemon2['point_de_vie'])
                self.pokemon1_attaque = False

            if self.pokemon2 and self.pokemon2['point_de_vie'] <= 0:
                gagnant_surface = self.font.render(f"{self.pokemon1['nom']} a gagné!", True, (0, 255, 0))
                perdant_surface = self.font.render(f"{self.pokemon2['nom']} a perdu!", True, (255, 0, 0))
                self.fenetre.blit(gagnant_surface, (20, self.hauteur_fenetre - 50))
                self.fenetre.blit(perdant_surface, (400, self.hauteur_fenetre - 50))

            if self.pokemon1 and self.pokemon1['point_de_vie'] <= 0:
                gagnant_surface = self.font.render(f"{self.pokemon2['nom']} a gagné!", True, (0, 255, 0))
                perdant_surface = self.font.render(f"{self.pokemon1['nom']} a perdu!", True, (255, 0, 0))
                self.fenetre.blit(gagnant_surface, (20, self.hauteur_fenetre - 50))
                self.fenetre.blit(perdant_surface, (400, self.hauteur_fenetre - 50))

            pygame.display.flip()

            gagnant = self.determiner_gagnant()
            if gagnant != "Match nul":
                print(f"Le gagnant est {gagnant}!")
            else:
                print("Match nul!")


if __name__ == "__main__":
    battle_instance = Battle()
    battle_instance.run()

