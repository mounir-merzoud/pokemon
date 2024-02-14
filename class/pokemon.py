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
