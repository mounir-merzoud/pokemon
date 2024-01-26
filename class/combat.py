import pygame
import random
import sys


pygame.init()

# Paramètres de la fenêtre
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 30

# Couleurs
WHITE = (255, 255, 255)
<<<<<<< HEAD
=======
RED = (255, 0, 0)
BLACK = (0, 0, 0)
>>>>>>> 94164f02a6e0c40287163bd54fd8bebb39abe893

# Création de la fenêtre
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pokemon combat")

# Police pour le texte
<<<<<<< HEAD
font = pygame.font.Font(None, 36)
=======
font = pygame.font.Font(None, 24)
>>>>>>> 94164f02a6e0c40287163bd54fd8bebb39abe893

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
<<<<<<< HEAD

    def draw(self):
        pygame.draw.circle(window, (255, 0, 0), (self.x, self.y), 20)
        draw_text(self.name, self.x - 20, self.y + 30)
=======
        self.attack_weapon_name = ""

    def draw(self):
        pygame.draw.circle(window, RED, (self.x, self.y), 20)

        # Afficher les informations du Pokémon
        draw_text(self.name, self.x - 140, self.y - 60, BLACK, bold=True)  
        # Nom du Pokémon en gras
        draw_text(f"Level: {self.level}", self.x - 140, self.y - 40, BLACK)
        draw_text(f"Attaque: {self.attack_weapon.power}", self.x - 140, self.y - 20, BLACK)
        draw_text(f"Défense: {self.defense_weapon.power}", self.x - 140, self.y, BLACK)
        draw_text(f"Dégâts subis: {self.level * 10 - self.health}", self.x - 140, self.y + 20, BLACK)

        # Afficher l'arme utilisée à la dernière attaque
        draw_text(f"Arme: {self.attack_weapon_name}", self.x - 140, self.y + 40, BLACK)

    def move(self, dx, dy):
        # Vérifier que la nouvelle position reste à l'intérieur du cadre
        new_x = max(50, min(WINDOW_WIDTH - 100, self.x + dx))
        new_y = max(50, min(WINDOW_HEIGHT - 100, self.y + dy))
        self.x, self.y = new_x, new_y
>>>>>>> 94164f02a6e0c40287163bd54fd8bebb39abe893

    def attack(self, opponent):
        attack_power = self.attack_weapon.attack()
        effectiveness = self.calculate_effectiveness(opponent.type)
        damage = (self.level * attack_power * effectiveness) // 10
        opponent.receive_damage(damage)
<<<<<<< HEAD

        print(f"{self.name} attaque avec {self.attack_weapon.name} !")
        print(f"{opponent.name} subit {damage} points de degats.")
=======
        
        # Enregistrer le nom de l'arme utilisée
        self.attack_weapon_name = self.attack_weapon.name
        
        return f"{self.name} attaque avec {self.attack_weapon.name} ! {opponent.name} subit {damage} points de dégâts."
>>>>>>> 94164f02a6e0c40287163bd54fd8bebb39abe893

    def receive_damage(self, damage):
        defense_power = self.defense_weapon.defense()
        damage_taken = max(0, damage - defense_power)
        self.health -= damage_taken
<<<<<<< HEAD

        print(f"{self.name} recoit {damage_taken} points de degats.")

=======
>>>>>>> 94164f02a6e0c40287163bd54fd8bebb39abe893
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

<<<<<<< HEAD
def draw_text(text, x, y):
    text_surface = font.render(text, True, WHITE)
=======
def draw_text(text, x, y, color, bold=False):
    text_surface = font.render(text, True, color)
    if bold:
        text_surface = pygame.font.Font(None, 24).render(text, True, color)
>>>>>>> 94164f02a6e0c40287163bd54fd8bebb39abe893
    window.blit(text_surface, (x, y))

# Fonction pour rendre le plateau de jeu
def draw_board():
    window.fill(WHITE)
    pygame.draw.rect(window, (0, 0, 0), (50, 50, WINDOW_WIDTH - 100, WINDOW_HEIGHT - 100), 2)

<<<<<<< HEAD
=======
# Chargement des données depuis les fichiers JSON
with open('pokedex.json', 'r') as f:
    pokedex_data = json.load(f)

with open('donnees_pokemon.json', 'r') as f:
    pokemon_data = json.load(f)





>>>>>>> 94164f02a6e0c40287163bd54fd8bebb39abe893
# Boucle de jeu
running = True
clock = pygame.time.Clock()

<<<<<<< HEAD
# Création des Pokémon
dracaufeu = Pokemon("Dracaufeu", "Feu/Vol", 75, Weapon("Lance-Flammes", 10), Defense("Ecailles", 8), WINDOW_WIDTH - 100, 100)
leviator = Pokemon("Leviator", "Eau/Vol", 78, Weapon("Hydrocanon", 9), Defense("Ecailles", 8), 100, WINDOW_HEIGHT - 100)

=======
>>>>>>> 94164f02a6e0c40287163bd54fd8bebb39abe893
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

<<<<<<< HEAD
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
=======
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dracaufeu.move(-5, 0)
    if keys[pygame.K_RIGHT]:
        dracaufeu.move(5, 0)
    if keys[pygame.K_UP]:
        dracaufeu.move(0, -5)
    if keys[pygame.K_DOWN]:
        dracaufeu.move(0, 5)
>>>>>>> 94164f02a6e0c40287163bd54fd8bebb39abe893

    # Combat
    result = dracaufeu.attack(leviator)
    draw_text(result, 20, 20, BLACK)

    result = leviator.attack(dracaufeu)
    draw_text(result, 50, 80, BLACK)

    # Rendu du plateau de jeu
    draw_board()

    # Afficher les Pokémon
    dracaufeu.draw()
    leviator.draw()

    # Mis à jour de l'affichage
    pygame.display.flip()
    clock.tick(FPS)
<<<<<<< HEAD
=======

>>>>>>> 94164f02a6e0c40287163bd54fd8bebb39abe893
