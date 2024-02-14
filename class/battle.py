# battle.py
import pygame
import json
import sys
<<<<<<< HEAD
from choix_de_pokemon import GestionPokemon
from barre_de_vie import *
import random
=======
import random

from barre_de_vie import BarreDeVie
from pokemon import Pokemon
from choix_de_pokemon import Menu
from pokedex import*

>>>>>>> main

class Battle:
    def __init__(self, pokedex_instance):
        pygame.init()

        self.largeur_fenetre = 800
        self.hauteur_fenetre = 600

        self.fenetre = pygame.display.set_mode((self.largeur_fenetre, self.hauteur_fenetre))
        pygame.display.set_caption("Battle")

        self.font = pygame.font.Font(None, 24)

<<<<<<< HEAD
        self.pokedex_instance = pokedex_instance

        self.pokemon1_attaque = False
        self.pokemon2_attaque = False
=======
        # Chargement de l'image de fond
        self.image_fond = pygame.image.load("images/background.png")
        self.image_fond = pygame.transform.scale(self.image_fond, (self.largeur_fenetre, self.hauteur_fenetre))
>>>>>>> main

        self.pokemon1 = None
        self.pokemon2 = None

        self.barre_vie_pokemon1 = BarreDeVie(20, 160, (0, 255, 0))
        self.barre_vie_pokemon2 = BarreDeVie(400, 160, (255, 0, 0))

        self.temps_de_jeu = 120  # Durée du combat en secondes
        self.temps_depart = pygame.time.get_ticks()  # Heure de début du combat

        self.pokedex = Pokedex("pokedex.json")

        # Position d'affichage du nom du Pokémon gagnant et perdant
        self.position_nom_gagnant_perdant = (self.largeur_fenetre // 2, 50)

    def afficher_nom_gagnant_perdant(self, gagnant, perdant):
        nom_gagnant = self.font.render(f"Gagnant: {gagnant}", True, (0, 255, 0))
        nom_perdant = self.font.render(f"Perdant: {perdant}", True, (255, 0, 0))
        self.fenetre.blit(nom_gagnant, (self.position_nom_gagnant_perdant[0] - nom_gagnant.get_width() // 2, self.position_nom_gagnant_perdant[1]))
        self.fenetre.blit(nom_perdant, (self.position_nom_gagnant_perdant[0] - nom_perdant.get_width() // 2, self.position_nom_gagnant_perdant[1] + 30))

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
<<<<<<< HEAD
        if self.pokemon1['point_de_vie'] <= 0 and self.pokemon2['point_de_vie'] > 0:
            return self.pokemon2
        elif self.pokemon2['point_de_vie'] <= 0 and self.pokemon1['point_de_vie'] > 0:
            return self.pokemon1
=======
        if self.pokemon1.point_de_vie <= 0 and self.pokemon2.point_de_vie > 0:
            return self.pokemon2.nom
        elif self.pokemon2.point_de_vie <= 0 and self.pokemon1.point_de_vie > 0:
            return self.pokemon1.nom
>>>>>>> main
        else:
            return None

    def pokemon_rencontre(self):
        pokemons_disponibles = ['Pikachu', 'Bulbasaur', 'Charmander', 'Squirtle']  # Liste des Pokémon disponibles
        pokemon_rencontre = random.choice(pokemons_disponibles)  # Choix aléatoire d'un Pokémon
        self.pokedex_instance.add_to_pokedex(pokemon_rencontre)  # Ajouter le Pokémon rencontré au Pokédex
        return pokemon_rencontre

    def run(self):
        with open("pokemon_choisi_aleatoirement.json", "r") as file1, open("pokemon_selectionne.json", "r") as file2:
            donnees_pokemon1 = json.load(file1)
            donnees_pokemon2 = json.load(file2)

        # Sélectionner un Pokémon au hasard à partir des données chargées
        pokemon1_nom = random.choice(list(donnees_pokemon1.keys()))
        pokemon2_nom = "selected_pokemon"  # Utilisation du nom du Pokémon sélectionné

        # Charger les Pokémon à partir des données
        self.pokemon1 = self.charger_pokemon(pokemon1_nom, donnees_pokemon1)
        self.pokemon2 = self.charger_pokemon(pokemon2_nom, donnees_pokemon2)

        while True:
            temps_ecoule = (pygame.time.get_ticks() - self.temps_depart) /1000 # Calcul du temps écoulé en secondes

            if temps_ecoule >= self.temps_de_jeu:
                print("Le temps est écoulé!")
                break

            # Affichage de l'image de fond
            self.fenetre.blit(self.image_fond, (0, 0))

            if self.pokemon1:
                # Affichage du Pokémon 1
                self.barre_vie_pokemon1.update_vie(self.pokemon1.point_de_vie)
                self.barre_vie_pokemon1.afficher(self.fenetre, self.pokemon1.point_de_vie)
                chemin_image_pokemon1 = f"images/{self.pokemon1.images}"  # Récupérer le chemin de l'image
                image_pokemon1 = pygame.image.load(chemin_image_pokemon1)
                image_pokemon1 = pygame.transform.scale(image_pokemon1, (100, 100))
                self.fenetre.blit(image_pokemon1, (60, 450))  # Afficher l'image du Pokémon

            if self.pokemon2:
                # Affichage du Pokémon 2
                self.barre_vie_pokemon2.update_vie(self.pokemon2.point_de_vie)
                self.barre_vie_pokemon2.afficher(self.fenetre, self.pokemon2.point_de_vie)
                chemin_image_pokemon2 = f"images/{self.pokemon2.images}"  # Récupérer le chemin de l'image
                image_pokemon2 = pygame.image.load(chemin_image_pokemon2)
                image_pokemon2 = pygame.transform.scale(image_pokemon2, (100, 100))
                self.fenetre.blit(image_pokemon2, (550, 280))  # Afficher l'image du Pokémon

            if self.pokemon2 and self.pokemon1:
                print(f"{self.pokemon2.nom} attaque avec {self.pokemon2.type_dattaque}")
                self.attaquer(self.pokemon2, self.pokemon1)
                if self.pokemon1:
                    self.barre_vie_pokemon1.update_vie(self.pokemon1.point_de_vie)
                    self.barre_vie_pokemon1.afficher(self.fenetre, self.pokemon1.point_de_vie)

                pygame.time.delay(1000)  # Ajout d'un délai de 1 seconde entre les attaques

                print(f"{self.pokemon1.nom} attaque avec {self.pokemon1.type_dattaque}")
                self.attaquer(self.pokemon1, self.pokemon2)
                if self.pokemon2:
                    self.barre_vie_pokemon2.update_vie(self.pokemon2.point_de_vie)
                    self.barre_vie_pokemon2.afficher(self.fenetre, self.pokemon2.point_de_vie)

                pygame.time.delay(1000)  # Ajout d'un délai de 1 seconde entre les attaques

            pygame.display.flip()

            gagnant = self.determiner_gagnant()
<<<<<<< HEAD
            if gagnant:
                print(f"Le gagnant est {gagnant['nom']}!")
                perdant = self.pokemon1 if gagnant != self.pokemon1 else self.pokemon2
                self.pokedex_instance.add_to_pokedex(gagnant['nom'])
                self.pokedex_instance.add_to_pokedex(perdant['nom'])
            else:
                print("Match nul!")

=======
            if gagnant != "Match nul":
                print(f"Le gagnant est {gagnant}!")
                self.pokedex.enregistrer_pokemon_perdant(gagnant)
                # Afficher le nom du gagnant et du perdant en haut de la fenêtre
                self.afficher_nom_gagnant_perdant(gagnant, self.pokemon1.nom if gagnant == self.pokemon2.nom else self.pokemon2.nom)
                break

            pygame.time.delay(100)  # Délai pour limiter le taux de rafraîchissement de l'affichage

>>>>>>> main
if __name__ == "__main__":
    from pokedex import Pokedex
    pokedex = Pokedex()
    battle_instance = Battle(pokedex)
    battle_instance.run()
