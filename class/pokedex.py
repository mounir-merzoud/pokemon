import json

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
pokedex.add_pokemon("Pikachu")
pokedex.add_pokemon("Charmander")
pokedex.add_pokemon("Pikachu")  # Cela devrait afficher un message de doublon
pokedex.display_all_pokemon()

# Sauvegarde du Pokedex dans un fichier JSON
pokedex.save_to_json()

# Chargement du Pokedex depuis le fichier JSON
pokedex.load_from_json()
pokedex.display_all_pokemon()