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
