import pygame
import sys
import random
import os

pygame.init()

class Map:
    def __init__(self, image_path, screen_width, screen_height, zoom_factor=3.0):
        self.original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.original_image, (int(screen_width * zoom_factor), int(screen_height * zoom_factor)))
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class Joueur:
    def __init__(self, image_path, screen_width, screen_height, player_width=60, player_height=60):
        self.original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.original_image, (player_width, player_height))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.speed = 0.2

    def move(self, keys):
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx -= self.speed
        if keys[pygame.K_RIGHT]:
            dx += self.speed
        if keys[pygame.K_UP]:
            dy -= self.speed
        if keys[pygame.K_DOWN]:
            dy += self.speed
        return dx, dy

# Chemins des images Pokémon
images_paths = [
    "images/p1.png",
    "images/p2.png",
    "images/p5.png",
    "images/p8.png",
    "images/p9.png",
    "images/p10.png",
    "images/p11.png",
    "images/p14.png",
    "images/p16.png",
]

# Positions fixes pour les images Pokémon
pokemon_positions = [
    (100, 100),
    (200, 150),
    (300, 200),
    (400, 250),
    (500, 300),
    (100, 350),
    (200, 400),
    (300, 450),
    (400, 500),
]

# Paramètres de la fenêtre
screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pokemon Map")

# Création de la carte avec une image JPG et un facteur de zoom plus grand
map_image_path = "images/Map.jpg"
pokemon_map = Map(map_image_path, screen_width, screen_height, zoom_factor=3.0)

# Création du joueur avec une image PNG et des dimensions spécifiques
joueur_image_path = "images/sacha.png"
joueur = Joueur(joueur_image_path, screen_width, screen_height, player_width=60, player_height=60)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gestion des touches
    keys = pygame.key.get_pressed()
    dx, dy = joueur.move(keys)

    # Déplacer la carte en fonction du joueur
    joueur.move(keys)
    pokemon_map.move(dx, dy)

    # Afficher la carte à partir de la position décalée
    screen.blit(pokemon_map.image, (pokemon_map.rect.x - pokemon_map.x, pokemon_map.rect.y - pokemon_map.y))

    # Afficher le joueur
    screen.blit(joueur.image, joueur.rect)

    # Vérifier si le joueur est sur la même position qu'une image Pokémon
    for path, (x, y) in zip(images_paths, pokemon_positions):
        pokemon_rect = pygame.Rect(x - pokemon_map.x, y - pokemon_map.y, 60, 60)  # Ajustez la taille selon vos besoins

        # Afficher l'image Pokémon à la position fixe
        pokemon_image = pygame.transform.scale(pygame.image.load(path), (60, 60))
        screen.blit(pokemon_image, (x - pokemon_map.x, y - pokemon_map.y))

        # Vérifier la collision avec le joueur
        if joueur.rect.colliderect(pokemon_rect):
            print("Combat!")  # Vous pouvez remplacer ceci par l'ouverture de la fenêtre de combat

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()
