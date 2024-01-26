<<<<<<< HEAD

import donnees_pokemon.json
from class.choix_de_pokemon import *
from map import *

import random

# Générer un nombre aleatoire entre 1 et 10
=======
import pygame
import random
import sys

pygame.init()

# Générer un nombre aleatoire entre 1 et 18
>>>>>>> bddf1f250fc171c1246ee79c9e16c41f7f76e732
nombre_aleatoire = random.randint(1, 18)

# Afficher le nombre generee
print("Nombre aleatoire :", nombre_aleatoire)

<<<<<<< HEAD
import pygame
import sys

pygame.init()

# Taille de la fenêtre
largeur, hauteur = 800, 600
taille_fenetre = (largeur, hauteur)

# Créer la fenêtre
fenetre = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption("Pokemon combat")

# Définir la couleur de fond
couleur_fond = (255, 255, 255)

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dessiner sur la fenêtre
    fenetre.fill(couleur_fond)

    # Mettre à jour l'affichage
    pygame.display.flip()
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

#Jeu
jeu = JeuPokemon()
nom_adversaire, type_adversaire = jeu.get_adversaire_info()
print(f"L'adversaire s'appelle {nom_adversaire} et est de type {type_adversaire}")

class Pokemon:
    def __init__(self, nom, puissance_attaque):
        self.nom = nom
        self.puissance_attaque = puissance_attaque

    def get_type(self):
        # Supposons que la méthode get_type() retourne le type du Pokémon
        return "TypePokemon"

class AttaqueEnnemi:
    def __init__(self):
        self.adversaire = Pokemon("Feu", 10)

    def get_adversaire_info(self):
        nom_adversaire = self.adversaire.nom
        type_adversaire = self.adversaire.get_type()
        return nom_adversaire, type_adversaire

    def calculer_degats(self):
        # Ajoutez votre logique pour calculer les dégâts en fonction du type d'attaque et du type de l'adversaire
        attaque = self.adversaire.puissance_attaque
        type_adversaire = self.adversaire.get_type()

        # Exemple de tableau de correspondance, ajustez selon vos besoins
        tableau_correspondance = {
            "Eau": {"Terre": 0.5, "Feu": 1.5},  # Exemple, ajustez selon les types de votre jeu
            # Ajoutez d'autres correspondances de types au besoin
        }

        multiplicateur = tableau_correspondance.get(type_adversaire, {}).get("Eau", 1.0)  # Par défaut, pas de modification
        degats = attaque * multiplicateur
        return degats

# Jeu
jeu = AttaqueEnnemi()
nom_adversaire, type_adversaire = jeu.get_adversaire_info()
degats = jeu.calculer_degats()

print(f"L'adversaire attaque {nom_adversaire} avec {type_adversaire} et inflige {degats} PV de degats.")


class Personnage:
    def __init__(self, points_de_vie, defense):
        self.points_de_vie = points_de_vie
        self.defense = defense

    def attaquer(self, attaque):
        degats = attaque - self.defense
        if degats > 0:
            self.points_de_vie -= degats
            print(f"Attaque reussie ! {degats} points de vie en moins.")
        else:
            print("L'attaque est bloquee par la defense.")


joueur = Personnage(points_de_vie=100, defense=10)
ennemi = Personnage(points_de_vie=80, defense=5)

# Attaque du joueur sur l'ennemi
attaque_joueur = 15
ennemi.attaquer(attaque_joueur)

# Attaque de l'ennemi sur le joueur
attaque_ennemi = 12
joueur.attaquer(attaque_ennemi)

# Affichage des points de vie restants
print(f"Points de vie du joueur : {joueur.points_de_vie}")
print(f"Points de vie de l'ennemi : {ennemi.points_de_vie}")

class Personnage:
    def __init__(self, nom, points_de_vie, defense):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.defense = defense

    def attaquer(self, attaque):
        degats = attaque - self.defense
        if degats > 0:
            self.points_de_vie -= degats
            print(f"Attaque reussie ! {degats} points de vie en moins pour {self.nom}.")
        else:
            print(f"L'attaque est bloquee par la defense de {self.nom}.")

    def est_en_vie(self):
        return self.points_de_vie > 0


def determiner_vainqueur(personnage1, personnage2):
    while personnage1.est_en_vie() and personnage2.est_en_vie():
        attaque1 = 15  # Remplacez cela par la méthode que vous utilisez pour calculer l'attaque du personnage1
        personnage2.attaquer(attaque1)

        if not personnage2.est_en_vie():
            return personnage1.nom

        attaque2 = 12  # Remplacez cela par la méthode que vous utilisez pour calculer l'attaque du personnage2
        personnage1.attaquer(attaque2)

        if not personnage1.est_en_vie():
            return personnage2.nom

    return "Match nul"


# Jeu
joueur1 = Personnage(nom="Joueur 1", points_de_vie=100, defense=10)
joueur2 = Personnage(nom="Joueur 2", points_de_vie=80, defense=5)

vainqueur = determiner_vainqueur(joueur1, joueur2)
print(f"Le vainqueur est {vainqueur}.")

import random

class Pokemon:
    def __init__(self, nom, points_de_vie, defense):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.defense = defense

    def attaquer(self):
        # Simuler une attaque avec une valeur aléatoire
        return random.randint(10, 20)

    def est_en_vie(self):
        return self.points_de_vie > 0


def determiner_vainqueur(pokemon1, pokemon2):
    while pokemon1.est_en_vie() and pokemon2.est_en_vie():
        attaque1 = pokemon1.attaquer()
        pokemon2.points_de_vie -= max(0, attaque1 - pokemon2.defense)
        print(f"{pokemon1.nom} attaque {pokemon2.nom} et lui inflige {max(0, attaque1 - pokemon2.defense)} points de vie.")

        if not pokemon2.est_en_vie():
            return pokemon1.nom, pokemon2.nom

        attaque2 = pokemon2.attaquer()
        pokemon1.points_de_vie -= max(0, attaque2 - pokemon1.defense)
        print(f"{pokemon2.nom} attaque {pokemon1.nom} et lui inflige {max(0, attaque2 - pokemon1.defense)} points de vie.")

        if not pokemon1.est_en_vie():
            return pokemon2.nom, pokemon1.nom

    return None, None  # Aucun vainqueur en cas de match nul


# Jeu
pokemon1 = Pokemon(nom="Pikachu", points_de_vie=100, defense=10)
pokemon2 = Pokemon(nom="Bulbasaur", points_de_vie=80, defense=5)

gagnant, perdant = determiner_vainqueur(pokemon1, pokemon2)

if gagnant and perdant:
    print(f"Le Pokemon gagnant est {gagnant}, et le Pokemon perdant est {perdant}.")
else:
    print("Match nul.")
=======
# Paramètres de la fenêtre
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 30

# Couleurs
WHITE = (255, 255, 255)

# Création de la fenêtre
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pokemon combat")

# Police pour le texte
font = pygame.font.Font(None, 36)

class Pokemon:
    def __init__(self, name, pokemon_type, level, attack_weapon, defense_weapon, x, y):
        self.name = name
        self.type = pokemon_type
        self.level = level
        self.attack_weapon = attack_weapon
        self.defense_weapon = defense_weapon
        self.health = level * 10
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.circle(window, (255, 0, 0), (self.x, self.y), 20)
        draw_text(self.name, self.x - 20, self.y + 30)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def attack(self, opponent):
        attack_power = self.attack_weapon.attack()
        effectiveness = self.calculate_effectiveness(opponent.type)
        damage = (self.level * attack_power * effectiveness) // 10
        opponent.receive_damage(damage)

        print(f"{self.name} attaque avec {self.attack_weapon.name} !")
        print(f"{opponent.name} subit {damage} points de degats.")

    def receive_damage(self, damage):
        defense_power = self.defense_weapon.defense()
        damage_taken = max(0, damage - defense_power)
        self.health -= damage_taken

        print(f"{self.name} recoit {damage_taken} points de degats.")

        if self.health < 0:
            self.health = 0

    def calculate_effectiveness(self, opponent_type):
        effectiveness_chart = {
            ('Feu', 'Eau'): 0.5,
            ('Eau', 'Feu'): 2.0,
            # Ajoutez d'autres relations de type selon besoin
        }

        if self.type == opponent_type:
            return 1.0
        elif (self.type, opponent_type) in effectiveness_chart:
            return effectiveness_chart[(self.type, opponent_type)]
        else:
            return 1.0

class Weapon:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        return random.randint(self.power // 2, self.power)

class Defense:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def defense(self):
        return random.randint(self.power // 2, self.power)

def draw_text(text, x, y):
    text_surface = font.render(text, True, WHITE)
    window.blit(text_surface, (x, y))

# Fonction pour rendre le plateau de jeu
def draw_board():
    window.fill(WHITE)
    pygame.draw.rect(window, (0, 0, 0), (50, 50, WINDOW_WIDTH - 100, WINDOW_HEIGHT - 100), 2)

# Boucle de jeu
running = True
clock = pygame.time.Clock()

# Création des Pokémon
dracaufeu = Pokemon("Dracaufeu", "Feu/Vol", 75, Weapon("Lance-Flammes", 10), Defense("Ecailles", 8), 100, 100)
leviator = Pokemon("Leviator", "Eau/Vol", 78, Weapon("Hydrocanon", 9), Defense("Ecailles", 8), 200, 200)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dracaufeu.move(-5, 0)
    if keys[pygame.K_RIGHT]:
        dracaufeu.move(5, 0)
    if keys[pygame.K_UP]:
        dracaufeu.move(0, -5)
    if keys[pygame.K_DOWN]:
        dracaufeu.move(0, 5)

    # Combat
    result = dracaufeu.attack(leviator)
    draw_text(result, 20, 20)

    result = leviator.attack(dracaufeu)
    draw_text(result, 20, 60)

    # Rendu du plateau de jeu
    draw_board()

    # Afficher les Pokémon
    dracaufeu.draw()
    leviator.draw()

    # Mettre à jour l'affichage
    pygame.display.flip()
    clock.tick(FPS)
>>>>>>> bddf1f250fc171c1246ee79c9e16c41f7f76e732
