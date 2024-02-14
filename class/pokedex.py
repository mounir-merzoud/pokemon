class Pokedex:
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
