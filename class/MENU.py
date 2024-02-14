import pygame  # Importation de la bibliothèque Pygame
import sys  # Importation du module sys pour les opérations système
from choix_de_pokemon import *  # Importation de classes ou fonctions depuis le fichier "choix_de_pokemon.py"

class Menu:  # Définition de la classe Menu
    def __init__(self):  # Définition du constructeur de classe
        pygame.init()  # Initialisation de Pygame

        # Définir la taille de la fenêtre
        self.screen = pygame.display.set_mode((800, 620))
        pygame.display.set_caption("Menu")  # Définir le titre de la fenêtre

        # Charger l'image de fond
        self.bg = pygame.image.load("images/background.jpeg")

        # Définir la police et la taille du texte
        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)

        # Définition des couleurs utilisées dans le menu
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)

        # Position et texte des boutons du menu
        self.button_positions = {
            'Nouvelle_partie': (50, 50),
            'Choisir_pokemon': (50, 100),
            'Acceder_pokedex': (50, 150),
            'Quitter_partie': (50, 200)
        }

        # Définition des actions associées à chaque bouton
        self.button_actions = {
            'Nouvelle_partie': self.Nouvelle_partie,
            'Choisir_pokemon': self.Choisir_pokemon,
            'Acceder_pokedex': self.Acceder_pokedex,
            'Quitter_partie': self.Quitter_partie
        }

    # Méthodes pour les actions des boutons
    def Nouvelle_partie(self):  # Action pour le bouton "Nouvelle_partie"
        from map import Map  # Importation de la classe Map
        nouvelle_partie_map = Map()  # Création d'une instance de la classe Map
        nouvelle_partie_map.run()  # Exécution de la méthode run de l'instance Map

    def Choisir_pokemon(self):  # Action pour le bouton "Choisir_pokemon"
        gestion_pokemon = GestionPokemon("donnees_pokemon.json", 620)  # Création d'une instance de la classe GestionPokemon
        gestion_pokemon.run(self.screen)  # Exécution de la méthode run de l'instance GestionPokemon

    def Acceder_pokedex(self):  # Action pour le bouton "Acceder_pokedex"
        print("Entrer sur le Pokédex")

    def Quitter_partie(self):  # Action pour le bouton "Quitter_partie"
        pygame.quit()  # Fermeture de Pygame
        sys.exit()  # Sortie du programme

    # Vérifier si la souris survole un bouton
    def check_button_hover(self, mouse_pos, button_rect):
        return button_rect.collidepoint(mouse_pos)

    # Gérer les clics de bouton
    def handle_button_click(self, button_name):
        if button_name in self.button_actions:
            self.button_actions[button_name]()

    # Boucle principale du menu
    def run(self):
        while True:
            # Afficher l'arrière-plan
            self.screen.blit(self.bg, (0, 0))

            for event in pygame.event.get():  # Parcourir les événements pygame
                if event.type == pygame.QUIT:  # Si l'événement est de quitter la fenêtre
                    self.Quitter_partie()  # Appeler la méthode Quitter_partie

                elif event.type == pygame.MOUSEBUTTONDOWN:  # Si un bouton de la souris est cliqué
                    for button_name, button_position in self.button_positions.items():
                        # Correction : Utilisation de self.font.size pour obtenir la taille du texte
                        button_rect = pygame.Rect(button_position, self.font.size(button_name))
                        if button_rect.collidepoint(event.pos):
                            self.handle_button_click(button_name)

            mouse_pos = pygame.mouse.get_pos()  # Obtenir la position actuelle de la souris

            # Mettre à jour la couleur du texte et du fond en fonction du survol
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

            pygame.display.flip()  # Mettre à jour l'affichage

if __name__ == "__main__":
    menu = Menu()  # Création d'une instance de la classe Menu
    menu.run()  # Exécution de la méthode run de l'instance Menu
