import pygame
import sys
from MENU import Menu  # Assurez-vous que la classe Menu est définie dans votre fichier MENU.py
from battle import Battle

pygame.init()

class Map:
    def __init__(self, map_image_path, screen_width, screen_height, zoom_factor=3.0):
        self.original_image = pygame.image.load(map_image_path)
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

images_paths = [
<<<<<<< HEAD
    "images/p1.png",
    #"images/p2.png",
   #"images/p5.png",
   #"images/p8.png",
   #"images/p9.png",
   #"images/p10.png",
   #"images/p11.png",
   #"images/p14.png",
   #"images/p16.png",
=======
    "images/beedrill.png",
    # Ajoutez d'autres chemins d'images Pokémon ici
>>>>>>> f12e38fb3a6e35d3e6a6902247a522f1c066a4c7
]

pokemon_positions = [
    (100, 100),
    (200, 100),
    (300, 100),
    (400, 250),
    (500, 300),
    (100, 350),
    (200, 400),
    (300, 450),
    (400, 500),
]

screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pokemon Map")

map_image_path = "images/Map.jpg"
pokemon_map = Map(map_image_path, screen_width, screen_height, zoom_factor=3.0)

joueur_image_path = "images/sacha.png"
joueur = Joueur(joueur_image_path, screen_width, screen_height, player_width=60, player_height=60)

back_button_rect = pygame.Rect(20, 20, 80, 40)
back_button_text = pygame.font.Font(None, 36).render("Back", True, (255, 255, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and back_button_rect.collidepoint(event.pos):
            menu = Menu()
            menu.run()

    keys = pygame.key.get_pressed()
    dx, dy = joueur.move(keys)

    joueur.move(keys)
    pokemon_map.move(dx, dy)

    screen.blit(pokemon_map.image, (pokemon_map.rect.x - pokemon_map.x, pokemon_map.rect.y - pokemon_map.y))
    screen.blit(joueur.image, joueur.rect)

    for path, (x, y) in zip(images_paths, pokemon_positions):
        pokemon_rect = pygame.Rect(x - pokemon_map.x, y - pokemon_map.y, 60, 60)

        pokemon_image = pygame.transform.scale(pygame.image.load(path), (5, 5))
        screen.blit(pokemon_image, (x - pokemon_map.x, y - pokemon_map.y))

        if joueur.rect.colliderect(pokemon_rect):
            print("Combat!")
            # Vous pouvez remplacer ceci par l'ouverture de la fenêtre de combat
            battle_instance = Battle()
            battle_instance.run()

    pygame.draw.rect(screen, (0, 0, 0), back_button_rect)
    screen.blit(back_button_text, (30, 30))

    pygame.display.flip()

pygame.quit()
sys.exit()
