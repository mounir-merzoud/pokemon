import pygame
import json
#from combat import *

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
            if self.pokemon not in self.pokedex:
                self.pokedex.append(self.pokemon)
    
            
        
    
        
        
       
pokedex = Pokedex()
pokedex.creation_json()
pokedex.pokemon_debut()