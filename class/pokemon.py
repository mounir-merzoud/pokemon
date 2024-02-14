class Pokemon:  # Définition de la classe Pokemon
    def __init__(self, nom, images, niveau, type_dattaque, point_de_vie, puissance_dattaque, defense):
        # Méthode d'initialisation de la classe Pokemon avec ses attributs
        self.nom = nom  # Attribut pour stocker le nom du Pokémon
        self.images = images  # Attribut pour stocker le chemin vers l'image du Pokémon
        self.niveau = niveau  # Attribut pour stocker le niveau du Pokémon
        self.type_dattaque = type_dattaque  # Attribut pour stocker le type d'attaque du Pokémon
        self.point_de_vie = point_de_vie  # Attribut pour stocker les points de vie du Pokémon
        self.puissance_dattaque = puissance_dattaque  # Attribut pour stocker la puissance d'attaque du Pokémon
        self.defense = defense  # Attribut pour stocker la défense du Pokémon

    def attaquer(self, cible):
        # Méthode pour faire attaquer le Pokémon à une cible
        degat = self.calculate_damage(cible)  # Calcul des dégâts infligés à la cible par le Pokémon
        print(f"{self.nom} attaque avec {self.type_dattaque} ! Dégâts infligés : {degat}")  # Affichage de l'attaque et des dégâts infligés
        cible.apply_damage(degat)  # Application des dégâts à la cible

    def apply_damage(self, damage):
        # Méthode pour appliquer les dégâts au Pokémon
        print(f"Avant l'attaque - Points de vie de {self.nom} : {self.point_de_vie}")  # Affichage des points de vie avant l'attaque
        self.point_de_vie -= damage  # Réduction des points de vie du Pokémon par les dégâts infligés
        print(f"Après l'attaque - Points de vie de {self.nom} : {self.point_de_vie}")  # Affichage des points de vie après l'attaque

    def calculate_damage(self, cible):
        # Méthode pour calculer les dégâts infligés à la cible en fonction du type d'attaque du Pokémon
        if self.type_dattaque == "eau":
            degat = 15
        elif self.type_dattaque == "terre":
            degat = 10
        elif self.type_dattaque == "feu":
            degat = 20
        elif self.type_dattaque == "normal":
            degat = 5
        return degat  # Retourne les dégâts calculés en fonction du type d'attaque du Pokémon
