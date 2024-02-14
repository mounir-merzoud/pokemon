<<<<<<< HEAD
import json
from pokemon import *
class Pokedex:
    def __init__(self):
        self.encountered_pokemon = []

    def add_pokemon(self, name):
        # Vérification des doublons avant d'ajouter le Pokémon
        if name not in self.encountered_pokemon:
            self.encountered_pokemon.append(name)
            print(f"{name} a été ajouté au Pokedex.")
        else:
            print(f"{name} est déjà dans le Pokedex.")
        
    def display_all_pokemon(self):
        # Affiche tous les Pokémon du Pokedex
        print("Pokémon rencontrés :")
        for pokemon in self.encountered_pokemon:
            print(pokemon)
        print(f"Nombre total de Pokémon rencontrés : {len(self.encountered_pokemon)}")
        
    def save_to_json(self):
        # Sauvegarde les données du Pokedex dans un fichier JSON
        with open('pokedex.json', 'w') as json_file:
            json.dump(self.encountered_pokemon, json_file)
            print("Pokedex sauvegardé avec succès")

    def load_from_json(self):
        # Charge les données du fichier JSON dans le Pokedex
        try:
            with open('pokedex.json', 'r') as json_file:
                data = json.load(json_file)
                self.encountered_pokemon = data
                print("Pokedex chargé avec succès.")
        except FileNotFoundError:
            print("Aucun fichier Pokedex trouvé.")

# Exemple d'utilisation
pokedex = Pokedex()
pokedex.add_pokemon("Salameche")
pokedex.add_pokemon("Carapuce")
# Sauvegarde du Pokedex dans un fichier JSON
pokedex.save_to_json()
# Chargement du Pokedex depuis le fichier JSON
pokedex.load_from_json()
pokedex.display_all_pokemon()
=======
import pygame
import json
import os

blanc = (255, 255, 255)

class Pokedex:
    def __init__(self, fichier_json, hauteur_fenetre):
        self.pokemon_data = self.charger_donnees(fichier_json)
        self.police = pygame.font.Font(None, 36)  # Déplacer cette ligne après l'initialisation de Pygame
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
            chemin_image = os.path.join("images", details.get("images", ""))
            if os.path.exists(chemin_image):
                image = pygame.image.load(chemin_image)
                self.images_pokemon[nom] = pygame.transform.scale(image, (50, 50))

    def afficher_boutons_pokemon(self, surface):
        for i, (nom, details) in enumerate(list(self.pokemon_data.items())[self.scroll_offset:self.scroll_offset + self.lignes_visibles]):
            y_position = self.y_position + i * 80
            bouton_rect = pygame.Rect(50, y_position + 10, 50, 50)
            pygame.draw.rect(surface, blanc, bouton_rect, 2)

            texte_nom = self.police.render(f"Nom: {details.get('nom', '')}", True, blanc)
            surface.blit(texte_nom, (120, y_position))
            texte_niveau = self.police.render(f"Niveau: {details.get('niveau', '')}", True, blanc)
            surface.blit(texte_niveau, (120, y_position + 30))

            if nom in self.images_pokemon:
                surface.blit(self.images_pokemon[nom], (50, y_position + 10))

        pygame.draw.rect(surface, blanc, self.nouveau_bouton_rect, 2)
        texte_nouveau_bouton = self.police.render("back", True, blanc)
        surface.blit(texte_nouveau_bouton, (self.nouveau_bouton_rect.x + 10, self.nouveau_bouton_rect.y + 10))

    def afficher_informations_pokemon(self, surface):
        if self.pokemon_selectionne:
            pygame.draw.rect(surface, blanc, (350, 50, 350, 200), 2)

            texte_nom = self.police.render(f"Nom: {self.pokemon_selectionne.get('nom', '')}", True, blanc)
            surface.blit(texte_nom, (380, 60))

            texte_niveau = self.police.render(f"Niveau: {self.pokemon_selectionne.get('niveau', '')}", True, blanc)
            surface.blit(texte_niveau, (380, 90))

            texte_type_attaque = self.police.render(f"Type d'attaque: {self.pokemon_selectionne.get('type_dattaque', '')}", True, blanc)
            surface.blit(texte_type_attaque, (380, 120))

            texte_point_de_vie = self.police.render(f"Point de vie: {self.pokemon_selectionne.get('point_de_vie', '')}", True, blanc)
            surface.blit(texte_point_de_vie, (380, 150))

            texte_puissance_attaque = self.police.render(f"Puissance d'attaque: {self.pokemon_selectionne.get('puissance_dattaque', '')}", True, blanc)
            surface.blit(texte_puissance_attaque, (380, 180))

            texte_defense = self.police.render(f"Défense: {self.pokemon_selectionne.get('defense', '')}", True, blanc)
            surface.blit(texte_defense, (380, 210))

    def select_pokemon(self, nom):
        print(f"Pokémon sélectionné : {nom}")
        self.pokemon_selectionne = self.pokemon_data.get(nom)

    def run(self):
        pygame.init()  # Initialisation de Pygame

        largeur_fenetre = 800
        hauteur_fenetre = 600
        fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
        pygame.display.set_caption("Pokedex")

        continuer = True
        while continuer:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continuer = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.nouveau_bouton_rect.collidepoint(event.pos):
                        print("Bouton 'back' cliqué.")
                        continuer = False

            fenetre.fill((0, 0, 0))
            self.afficher_boutons_pokemon(fenetre)
            self.afficher_informations_pokemon(fenetre)
            pygame.display.flip()

        pygame.quit()

class PokedexManager:
    def __init__(self, fichier_pokedex):
        self.fichier_pokedex = fichier_pokedex

    def charger_pokedex(self):
        try:
            with open(self.fichier_pokedex, "r") as fichier:
                data = fichier.read()
                if data:
                    return json.loads(data)
                else:
                    print("Le fichier pokedex.json est vide.")
                    return []
        except FileNotFoundError:
            print("Le fichier pokedex.json n'existe pas.")
            return []
        except json.decoder.JSONDecodeError:
            print("Le fichier pokedex.json contient des données invalides.")
            return []

    def enregistrer_pokemon_perdant(self, pokemon_perdant):
        pokedex = self.charger_pokedex()
        pokedex.append(pokemon_perdant)
        with open(self.fichier_pokedex, "w") as fichier:
            json.dump(pokedex, fichier)

if __name__ == "__main__":
    pokedex_manager = PokedexManager("pokedex.json")
    pokedex_manager.enregistrer_pokemon_perdant("pokemon_perdant")
    pokedex = Pokedex("pokedex.json", 600)
    pokedex.run()
>>>>>>> main
