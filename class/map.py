import pygame
import sys

class Map:
    def __init__(self, image_path, screen_width, screen_height, zoom_factor=3.0):
        # Charger l'image
        self.original_image = pygame.image.load(image_path)
        # Redimensionner l'image avec un facteur de zoom plus grand
        self.image = pygame.transform.scale(self.original_image, (int(screen_width * zoom_factor), int(screen_height * zoom_factor)))
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class Joueur:
    def __init__(self, image_path, screen_width, screen_height, player_width=50, player_height=50):
        # Charger l'image du joueur et redimensionner
        self.original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.original_image, (player_width, player_height))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.speed = 0.2 # Réduire la vitesse

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

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pokemon Map")

# Création de la carte avec une image JPG et un facteur de zoom plus grand
map_image_path = "images/Map.jpg"
pokemon_map = Map(map_image_path, screen_width, screen_height, zoom_factor=3.0)

# Création du joueur avec une image PNG et des dimensions spécifiques
joueur_image_path = "images/sacha.png"
joueur = Joueur(joueur_image_path, screen_width, screen_height, player_width=70, player_height=70)

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
    pokemon_map.move(dx, dy)

    # Afficher la carte à partir de la position décalée
    screen.blit(pokemon_map.image, (pokemon_map.rect.x - pokemon_map.x, pokemon_map.rect.y - pokemon_map.y))

    # Afficher le joueur
    screen.blit(joueur.image, joueur.rect)

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()
