import pygame
import sys
from choix_de_pokemon import *

class Menu:
    def __init__(self):
        pygame.init()

        # Définir la taille de la fenêtre
        self.screen = pygame.display.set_mode((800, 620))
        pygame.display.set_caption("Menu")

        # Charger l'image de fond
        self.bg = pygame.image.load("images/background.jpeg")

        # Définir la police et la taille du texte
        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)

        # Couleurs
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)

        # Position et texte des boutons
        self.button_positions = {
            'Nouvelle_partie': (50, 50),
            'Choisir_pokemon': (50, 100),
            'Acceder_pokedex': (50, 150),
            'Quitter_partie': (50, 200)
        }

        # Définir les actions des boutons
        self.button_actions = {
            'Nouvelle_partie': self.Nouvelle_partie,
            'Choisir_pokemon': self.Choisir_pokemon,
            'Acceder_pokedex': self.Acceder_pokedex,
            'Quitter_partie': self.Quitter_partie
        }

    def Nouvelle_partie(self):
        from map import Map
        nouvelle_partie_map = Map()
        nouvelle_partie_map.run()

    def Choisir_pokemon(self):
        gestion_pokemon = GestionPokemon("donnees_pokemon.json", 620)
        gestion_pokemon.run(self.screen)

    def Acceder_pokedex(self):
        print("Entrer sur le Pokédex")

    def Quitter_partie(self):
        pygame.quit()
        sys.exit()

    def check_button_hover(self, mouse_pos, button_rect):
        return button_rect.collidepoint(mouse_pos)

    def handle_button_click(self, button_name):
        if button_name in self.button_actions:
            self.button_actions[button_name]()

    def run(self):
        while True:
            # Afficher l'arrière-plan
            self.screen.blit(self.bg, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Quitter_partie()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button_name, button_position in self.button_positions.items():
                        # Correction : Utilisation de self.font.size pour obtenir la taille du texte
                        button_rect = pygame.Rect(button_position, self.font.size(button_name))
                        if button_rect.collidepoint(event.pos):
                            self.handle_button_click(button_name)

            mouse_pos = pygame.mouse.get_pos()

            # Mettez à jour la couleur du texte et du fond en fonction du survol
            for button_name, button_position in self.button_positions.items():
                # Correction : Utilisation de self.font.size pour obtenir la taille du texte
                button_rect = pygame.Rect(button_position, self.font.size(button_name))
                is_hovering = self.check_button_hover(mouse_pos, button_rect)

                # Couleur du texte
                text_color = self.red if is_hovering else self.black

                # Couleur du fond
                background_color = self.black if is_hovering else self.white

                # Créer une surface pour le fond avec une bordure arrondie
                button_surface = pygame.Surface((button_rect.width, button_rect.height), pygame.SRCALPHA)
                pygame.draw.rect(button_surface, background_color, button_surface.get_rect(), border_radius=10)
                button_surface.set_alpha(150)  # Ajuster la transparence du fond

                # Afficher le fond
                self.screen.blit(button_surface, button_rect.topleft)

                # Afficher le texte avec la couleur mise à jour
                text_surface = self.font.render(button_name, True, text_color)
                self.screen.blit(text_surface, button_rect.topleft)

                # Définir le curseur en fonction du survol
                if is_hovering:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            pygame.display.flip()

if __name__ == "__main__":
    menu = Menu()
    menu.run()
git 