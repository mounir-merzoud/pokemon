<<<<<<< HEAD
class Type:
    def __init__(self, nom, points_de_vie, puissance_attaque, defense):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.puissance_attaque = puissance_attaque
        self.defense = defense

    def attaquer(self, adversaire):
        degats = self.puissance_attaque - adversaire.defense
        print('ok')
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

# Combat entre les deux Pokémon
pokemon1.attaquer(pokemon2)
=======
class Pokemon:
    def __init__(self, nom, images, niveau, type_dattaque, point_de_vie, puissance_dattaque, defense):
        self.nom = nom
        self.images = images
        self.niveau = niveau
        self.type_dattaque = type_dattaque
        self.point_de_vie = point_de_vie
        self.puissance_dattaque = puissance_dattaque
        self.defense = defense

    def attaquer(self, cible):
        degat = self.calculate_damage(cible)
        print(f"{self.nom} attaque avec {self.type_dattaque} ! Dégâts infligés : {degat}")
        cible.apply_damage(degat)

    def apply_damage(self, damage):
        print(f"Avant l'attaque - Points de vie de {self.nom} : {self.point_de_vie}")
        self.point_de_vie -= damage
        print(f"Après l'attaque - Points de vie de {self.nom} : {self.point_de_vie}")

    def calculate_damage(self, cible):
        if self.type_dattaque == "eau":
            degat = 15
        elif self.type_dattaque == "terre":
            degat = 10
        elif self.type_dattaque == "feu":
            degat = 20
        elif self.type_dattaque == "normal":
            degat = 5
        return degat
>>>>>>> main
