class Combat:
    def __init__(self):
        # Tableau des multiplicateurs de puissance d'attaque en fonction du type d'adversaire
        self.types_adversaires = {
            'Eau': 1.5,
            'Feu': 2.0,
            'Terre': 1.2,
            'Normal': 1.8
        }

         # Tableau des multiplicateurs de puissance de defense en fonction du type d'adversaire
        self.types_adversaires = {
            'Eau': 1.5,
            'Feu': 2.0,
            'Terre': 1.2,
            'Normal': 1.8
        }

    def get_puissance_attaque(self, type_adversaire):
        # Vérifie si le type d'adversaire est présent dans le tableau
        if type_adversaire in self.types_adversaires:
            # Récupère le multiplicateur correspondant au type d'adversaire
            multiplicateur = self.types_adversaires[type_adversaire]
            # Demande à l'utilisateur de saisir la puissance d'attaque de l'adversaire
            puissance_attaque = float(input("Entrez la puissance d'attaque de l'adversaire : "))
            # Calcule la puissance d'attaque modifiée en fonction du type d'adversaire
            puissance_attaque_modifiee = puissance_attaque * multiplicateur
            # Affiche la puissance d'attaque modifiée
            print(f"La puissance d'attaque modifiée en fonction du type d'adversaire est : {puissance_attaque_modifiee}")
            return puissance_attaque_modifiee
        else:
            print("Type d'adversaire non reconnu.")
            return None

# Exemple d'utilisation de la classe Combat
combat_instance = Combat()
type_adversaire = input("Entrez le type de l'adversaire (Guerrier, Mage, Archer, Monstre) : ")
combat_instance.get_puissance_attaque(type_adversaire)
