import pygame
import sys
import json
import random
from barre_de_vie import *
from pokemon import *
from choix_de_pokemon import *

<<<<<<< HEAD
pygame.init()

# Paramètres de la fenêtre
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 30
=======
class Battle:
    def __init__(self):
        pygame.init()

        self.largeur_fenetre = 800
        self.hauteur_fenetre = 600

        self.fenetre = pygame.display.set_mode((self.largeur_fenetre, self.hauteur_fenetre))
        pygame.display.set_caption("Battle")
>>>>>>> combat

        self.font = pygame.font.Font(None, 24)

        self.pokemon1 = None
        self.pokemon2 = None

        self.barre_vie_pokemon1 = BarreDeVie(20, 160, (0, 255, 0))
        self.barre_vie_pokemon2 = BarreDeVie(400, 160, (255, 0, 0))

        self.temps_de_jeu = 60  # Durée du combat en secondes
        self.temps_depart = pygame.time.get_ticks()  # Heure de début du combat

    def charger_pokemon(self, nom_pokemon, donnees_pokemon):
        if nom_pokemon in donnees_pokemon:
            pokemon_data = donnees_pokemon[nom_pokemon]
            return Pokemon(**pokemon_data)
        else:
            print(f"Pokemon '{nom_pokemon}' non trouvé dans les données.")
            return None

    def attaquer(self, attaquant, cible):
        degat = self.calculate_damage(attaquant, cible)
        print(f"Dégâts infligés : {degat}")
        self.apply_damage(cible, degat)
        print(f"Points de vie de {cible.nom} après attaque : {cible.point_de_vie}")

    def apply_damage(self, pokemon, damage):
        print(f"Avant l'attaque - Points de vie de {pokemon.nom} : {pokemon.point_de_vie}")
        pokemon.point_de_vie -= damage
        print(f"Après l'attaque - Points de vie de {pokemon.nom} : {pokemon.point_de_vie}")

    def calculate_damage(self, attaquant, cible):
        if attaquant.type_dattaque == "eau":
            degat = 15
        elif attaquant.type_dattaque == "terre":
            degat = 10
        elif attaquant.type_dattaque == "feu":
            degat = 20
        elif attaquant.type_dattaque == "normal":
            degat = 5
        return degat

    def determiner_gagnant(self):
        if self.pokemon1.point_de_vie <= 0 and self.pokemon2.point_de_vie > 0:
            return self.pokemon2.nom
        elif self.pokemon2.point_de_vie <= 0 and self.pokemon1.point_de_vie > 0:
            return self.pokemon1.nom
        else:
            return "Match nul"

    def run(self):
        with open("pokemon_choisi_aleatoirement.json", "r") as file1, open("pokemon_selectionne.json", "r") as file2:
            donnees_pokemon1 = json.load(file1)
            donnees_pokemon2 = json.load(file2)

        # Sélectionner un Pokémon au hasard à partir des données chargées
        pokemon1_nom = random.choice(list(donnees_pokemon1.keys()))
        pokemon2_nom = "selected_pokemon"  # Utilisation du nom du Pokémon sélectionné

<<<<<<< HEAD
# Vérifier l'existence du fichier 'pokedex.json'
if not os.path.exists('pokedex.json'):
    print("Erreur: le fichier 'pokedex.json' est introuvable.")
    sys.exit()

# Chargement des données depuis les fichiers JSON
with open('pokedex.json', 'r') as f:
    pokedex_data = json.load(f)
=======
        # Charger les Pokémon à partir des données
        self.pokemon1 = self.charger_pokemon(pokemon1_nom, donnees_pokemon1)
        self.pokemon2 = self.charger_pokemon(pokemon2_nom, donnees_pokemon2)
>>>>>>> combat

        while True:
            temps_ecoule = (pygame.time.get_ticks() - self.temps_depart) / 1000  # Calcul du temps écoulé en secondes

<<<<<<< HEAD
# Création des Pokémon
dracaufeu = Pokemon("Dracaufeu", "Feu", 50, Weapon("Flamme", 40), Defense("Armure", 20), 100, 300)
leviator = Pokemon("Leviator", "Eau", 50, Weapon("Hydrocanon", 45), Defense("Ecailles", 25), 700, 300)
=======
            if temps_ecoule >= self.temps_de_jeu:
                print("Le temps est écoulé!")
                break

            self.fenetre.fill((255, 255, 255))

            if self.pokemon1:
                self.barre_vie_pokemon1.update_vie(self.pokemon1.point_de_vie)
                self.barre_vie_pokemon1.afficher(self.fenetre, self.pokemon1.point_de_vie)
                chemin_image_pokemon1 = f"images/{self.pokemon1.images}"  # Récupérer le chemin de l'image
                image_pokemon1 = pygame.image.load(chemin_image_pokemon1)
                image_pokemon1 = pygame.transform.scale(image_pokemon1, (100, 100))
                self.fenetre.blit(image_pokemon1, (20, 20))  # Afficher l'image du Pokémon

            if self.pokemon2:
                self.barre_vie_pokemon2.update_vie(self.pokemon2.point_de_vie)
                self.barre_vie_pokemon2.afficher(self.fenetre, self.pokemon2.point_de_vie)
                chemin_image_pokemon2 = f"images/{self.pokemon2.images}"  # Récupérer le chemin de l'image
                image_pokemon2 = pygame.image.load(chemin_image_pokemon2)
                image_pokemon2 = pygame.transform.scale(image_pokemon2, (100, 100))
                self.fenetre.blit(image_pokemon2, (400, 20))  # Afficher l'image du Pokémon
>>>>>>> combat

            if self.pokemon2 and self.pokemon1:
                print(f"{self.pokemon2.nom} attaque avec {self.pokemon2.type_dattaque}")
                self.attaquer(self.pokemon2, self.pokemon1)
                if self.pokemon1:
                    self.barre_vie_pokemon1.update_vie(self.pokemon1.point_de_vie)
                    self.barre_vie_pokemon1.afficher(self.fenetre, self.pokemon1.point_de_vie)

                print(f"{self.pokemon1.nom} attaque avec {self.pokemon1.type_dattaque}")
                self.attaquer(self.pokemon1, self.pokemon2)
                if self.pokemon2:
                    self.barre_vie_pokemon2.update_vie(self.pokemon2.point_de_vie)
                    self.barre_vie_pokemon2.afficher(self.fenetre, self.pokemon2.point_de_vie)

            pygame.display.flip()

            gagnant = self.determiner_gagnant()
            if gagnant != "Match nul":
                print(f"Le gagnant est {gagnant}!")
                break

<<<<<<< HEAD
    # Vérifier si le Pokémon attaqué a perdu tous ses points de vie
    if leviator.health <= 0:
        draw_text(f"{leviator.name} a perdu le combat !", 20, 50, BLACK)
        running = False

    result = leviator.attack(dracaufeu)
    draw_text(result, 50, 80, BLACK)

    # Vérifier si le Pokémon attaqué a perdu tous ses points de vie
    if dracaufeu.health <= 0:
        draw_text(f"{dracaufeu.name} a perdu le combat !", 20, 110, BLACK)
        running = False

    # Rendu du plateau de jeu
    draw_board()

    # Afficher les Pokémon
    dracaufeu.draw()
    leviator.draw()

    # Mis à jour de l'affichage
    pygame.display.flip()
    clock.tick(FPS)
=======
            pygame.time.delay(100)  # Délai pour limiter le taux de rafraîchissement de l'affichage

if __name__ == "__main__":
    battle_instance = Battle()
    battle_instance.run()
>>>>>>> combat
