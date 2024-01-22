import pygame
import random
import sys

pygame.init()

# Parametres de la fenetre
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
        return f"{self.name} attaque avec {self.attack_weapon.name} ! {opponent.name} subit {damage} points de degats."

    def receive_damage(self, damage):
        defense_power = self.defense_weapon.defense()
        damage_taken = max(0, damage - defense_power)
        self.health -= damage_taken
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

# Création des Pokemon
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

    # Mis à jour de l'affichage
    pygame.display.flip()
    clock.tick(FPS)
