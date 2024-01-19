class Pokemon:
    def __init__(self, nom, type):
        self.nom = nom
        self.type = type

    def get_type(self):
        return self.type

class JeuPokemon:
    def __init__(self):
        self.adversaire = Pokemon("Salameche", "Feu")

    def get_adversaire_info(self):
        nom_adversaire = self.adversaire.nom
        type_adversaire = self.adversaire.get_type()
        return nom_adversaire, type_adversaire

# Exemple d'utilisation
jeu = JeuPokemon()
nom_adversaire, type_adversaire = jeu.get_adversaire_info()
print(f"L'adversaire s'appelle {nom_adversaire} et est de type {type_adversaire}")
