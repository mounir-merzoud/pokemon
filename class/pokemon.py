import json
class Type:
    def __init__(self, nom, points_de_vie, puissance_attaque, defense):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.puissance_attaque = puissance_attaque
        self.defense = defense

    def attaquer(self, adversaire):
        degats = self.puissance_attaque - adversaire.defense
        if degats > 0:
            adversaire.enlever_points_de_vie(degats)

    def enlever_points_de_vie(self, degats):
        self.points_de_vie -= degats
        if self.points_de_vie < 0:
            self.points_de_vie = 0

    def evoluer(self):
        # Ajoutez ici la logique d'évolution du Pokémon selon vos critères.
        # Par exemple, augmentation du niveau, changement d'apparence, etc.
        pass

class Pokemon(Type):
    def __init__(self, nom, niveau, type_pokemon):
        super().__init__(type_pokemon.nom, type_pokemon.points_de_vie, type_pokemon.puissance_attaque, type_pokemon.defense)
        self.nom = nom
        self.niveau = niveau
        self.type_pokemon = type_pokemon

    # Vous pouvez ajouter des méthodes spécifiques pour les Pokémon si nécessaire.

# Exemple d'utilisation
type_feu = Type("Feu", 100, 30, 20)
pokemon1 = Pokemon("Salameche", 5, type_feu)

type_eau = Type("Eau", 120, 25, 25)
pokemon2 = Pokemon("Carapuce", 5, type_eau)

type_terre = Type("Terre", 80, 40, 10)
pokemon3 = Pokemon("Géodude", 10, type_terre)

type_normal = Type("Normal", 50, 50, 50)
pokemon4 = Pokemon("Rattata", 3, type_normal)


# Combat entre les deux Pokémon
#pokemon1.attaquer(pokemon2)
import json

def creer_fichier_json(nom_fichier, donnees):
    try:
        with open(nom_fichier, 'w') as fichier:
            json.dump(donnees, fichier, indent=2)
        print(f"Le fichier {nom_fichier} a été créé avec succès.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Créez les instances de Type et Pokemon
type_feu = Type("Feu", 100, 30, 20)
pokemon1 = Pokemon("Salameche", 5, type_feu)

type_eau = Type("Eau", 120, 25, 25)
pokemon2 = Pokemon("Carapuce", 5, type_eau)

type_terre = Type("Terre", 80, 40, 10)
pokemon3 = Pokemon("Géodude", 10, type_terre)

type_normal = Type("Normal", 50, 50, 50)
pokemon4 = Pokemon("Rattata", 3, type_normal)

# Créez une structure de dictionnaire pour stocker les données des Pokémon
donnees_pokemon = {
    "pokemon1": {
        "nom": pokemon1.nom,
        "niveau": pokemon1.niveau,
        "type": {
            "nom": pokemon1.type_pokemon.nom,
            "points_de_vie": pokemon1.type_pokemon.points_de_vie,
            "puissance_attaque": pokemon1.type_pokemon.puissance_attaque,
            "defense": pokemon1.type_pokemon.defense
        }
    },
    "pokemon2": {
        "nom": pokemon2.nom,
        "niveau": pokemon2.niveau,
        "type": {
            "nom": pokemon2.type_pokemon.nom,
            "points_de_vie": pokemon2.type_pokemon.points_de_vie,
            "puissance_attaque": pokemon2.type_pokemon.puissance_attaque,
            "defense": pokemon2.type_pokemon.defense
        }
    },
    "pokemon3": {
        "nom": pokemon3.nom,
        "niveau": pokemon3.niveau,
        "type": {
            "nom": pokemon3.type_pokemon.nom,
            "points_de_vie": pokemon3.type_pokemon.points_de_vie,
            "puissance_attaque": pokemon3.type_pokemon.puissance_attaque,
            "defense": pokemon3.type_pokemon.defense
        }
    },
    "pokemon4": {
        "nom": pokemon4.nom,
        "niveau": pokemon4.niveau,
        "type": {
            "nom": pokemon4.type_pokemon.nom,
            "points_de_vie": pokemon4.type_pokemon.points_de_vie,
            "puissance_attaque": pokemon4.type_pokemon.puissance_attaque,
            "defense": pokemon4.type_pokemon.defense
        }
    }
}

# Utilisez la fonction pour créer le fichier JSON
creer_fichier_json("donnees_pokemon.json", donnees_pokemon)
