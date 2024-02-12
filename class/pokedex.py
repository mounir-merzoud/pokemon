import pygame
import json
from battle import Battle  

pygame.init()

width = 800
height = 600
background = pygame.image.load('images/pokedex.jpg')
background = pygame.transform.scale(background, (width, height))

class Pokedex:
    
    def __init__(self):
        self.Data = {}
        with open('donnees_pokemon.json', 'r') as f:
            self.Data = json.load(f)
        self.pokedex = []

    def creation_json(self):
        with open('pokedex.json', 'w') as f:
            json.dump(self.pokedex, f, indent=2)

    def add_to_pokedex(self, pokemon_name):
        pokemon_data = self.Data.get(pokemon_name)
        if pokemon_data and pokemon_data not in self.pokedex:
            self.pokedex.append(pokemon_data)
            print(f"{pokemon_name} a été ajouté au Pokédex !")
            self.creation_json()

    def pokemon_debut(self):
        debut_pokemon = ['Weedle', 'Wartortle', 'Venusaur']
        for pokemon_name in debut_pokemon:
            self.add_to_pokedex(pokemon_name)

    def ajouter_pokemon_rencontre(self, pokedex_instance):
        combat = Battle(pokedex_instance)  

       
        self.pokemon_debut()

        # Ajouter les Pokémon rencontrés
        pokemon_rencontre = combat.pokemon_rencontre()  
        if pokemon_rencontre:
            self.add_to_pokedex(pokemon_rencontre)  

       
        self.creation_json()

       
        fenetre = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Pokedex")

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            fenetre.blit(background, (0, 0))
            y_position = 50
            for pokemon in self.pokedex:
                nom = pokemon['nom']
                niveau = pokemon['niveau']
                type_dattaque = pokemon['type_dattaque']
                texte_nom = pygame.font.Font(None, 24).render(f"Nom: {nom}", True, (0, 0, 0))
                texte_niveau = pygame.font.Font(None, 24).render(f"Niveau: {niveau}", True, (0, 0, 0))
                texte_type_dattaque = pygame.font.Font(None, 24).render(f"Type d'attaque: {type_dattaque}", True, (0, 0, 0))
                fenetre.blit(texte_nom, (50, y_position))
                fenetre.blit(texte_niveau, (50, y_position + 30))
                fenetre.blit(texte_type_dattaque, (50, y_position + 60))
                y_position += 100

            pygame.display.flip()

# Utilisez la même instance de Pokedex tout au long du programme
if __name__ == "__main__":
    pokedex = Pokedex()
    pokedex.ajouter_pokemon_rencontre(pokedex)  