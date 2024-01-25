import pygame
import json

class Pokedex:
    
    def __init__(self):
        
        self.Data = []
        with open ('donnees_pokemon.json', 'r' ) as f:
            self.Data=json.load(f)


        

    def creation_json(self):
        
        self.pokedex = []
        
        with open('pokedex.json','w') as f:
            json.dump(self.pokedex,f)

    
    #les 3 premiers pokemon de debut de jeu dans le pokedex
    def pokemon_debut(self):
        
        for i in range(3):
            self.pokemon = self.Data[f'pokemon{i+1}']
            with open('pokedex.json','r+') as f:
                self.pokedex=json.load(f)
                self.pokedex.append(self.pokemon)
                f.seek(0)
                print(i)
                json.dump(self.pokedex,f,indent=2)
        
        
    
        
        
          
pokedex = Pokedex()
pokedex.creation_json()
pokedex.pokemon_debut()




  

    # def save_to_json(self):
    #     with open('pokedex.json', 'w') as json_file:
    #         json.dump(self.pokedex, json_file, indent=2)
    #         print("Pokedex sauvegardé avec succès")

    # def load_from_json(self):
    #     try:
    #         with open('pokedex.json', 'r') as json_file:
    #             self.pokedex = json.load(json_file)
    #             print("Pokedex chargé avec succès.")
    #     except FileNotFoundError:
    #         print("Aucun fichier Pokedex trouvé.")
    
    # def get_pokemon_for_combat(self):
    #     return self.pokedex





# # Sauvegarde du Pokedex dans un fichier JSON
# pokedex.save_to_json()

# # Chargement du Pokedex depuis le fichier JSON
# pokedex.load_from_json()