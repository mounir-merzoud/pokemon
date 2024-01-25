import pygame
import sys
from choix_de_pokemon import GestionPokemon
from pokemon import Pokemon

class BarreDeVie:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.longueur_barre = 200
        self.largeur_barre = 20
        self.font = pygame.font.Font(None, 20)  # Police pour le texte des points de vie

    def afficher(self, surface, vie):
        vie_max = 100  # Vous pouvez ajuster cela en fonction de la santé maximale
        longueur_vie = int(self.longueur_barre * vie / vie_max)
        pygame.draw.rect(surface, (0, 0, 0), (self.x, self.y, self.longueur_barre, self.largeur_barre), 2)
        if vie > 0:
            pygame.draw.rect(surface, (0, 255, 0), (self.x, self.y, longueur_vie, self.largeur_barre))
            
            # Affichage du texte des points de vie
            texte_vie = self.font.render(str(vie), True, (0, 0, 0))
            surface.blit(texte_vie, (self.x + self.longueur_barre + 10, self.y))  # Ajustez la position du texte selon vos besoins

class PokemonBarreDeVie(BarreDeVie):
    def __init__(self, x, y, pokemon):
        super().__init__(x, y)
        self.pokemon = pokemon

    def afficher(self, surface):
        super().afficher(surface, self.pokemon['point_de_vie'])

class Battle:
    def __init__(self):
        pygame.init()

        self.largeur_fenetre = 800
        self.hauteur_fenetre = 600

        self.fenetre = pygame.display.set_mode((self.largeur_fenetre, self.hauteur_fenetre))
        pygame.display.set_caption("Battle")

        self.gestion_pokemon = GestionPokemon("donnees_pokemon.json", self.hauteur_fenetre)

        # Initialise la police
        self.font = pygame.font.Font(None, 24)

        self.pokemon1_attaque = False  # Indique si le premier Pokémon attaque
        self.pokemon2_attaque = False  # Indique si le deuxième Pokémon attaque

        # Pokémon en combat
        self.pokemon1 = None
        self.pokemon2 = None

        # Initialisation des barres de vie
        self.barre_vie_pokemon1 = None
        self.barre_vie_pokemon2 = None

    def attaquer(self, attaquant, cible):
        # Dégâts en fonction du type d'attaque
        if attaquant['type_dattaque'] == "eau":
            degat = 15
        elif attaquant['type_dattaque'] == "terre":
            degat = 10
        elif attaquant['type_dattaque'] == "feu":
            degat = 20
        else:
            degat = 5  # Normal

        cible["point_de_vie"] -= degat

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        # Détecter le clic sur l'image du premier Pokémon
                        if 150 <= event.pos[0] <= 250 and 350 <= event.pos[1] <= 450:
                            self.pokemon1_attaque = True
                            self.pokemon2_attaque = False
                        # Détecter le clic sur l'image du deuxième Pokémon
                        elif 550 <= event.pos[0] <= 650 and 350 <= event.pos[1] <= 450:
                            self.pokemon2_attaque = True
                            self.pokemon1_attaque = False

            pokemon1, pokemon2 = self.gestion_pokemon.charger_pokemon_combat("donnees_pokemon.json")

            self.fenetre.fill((255, 255, 255))

            if pokemon1:
                self.pokemon1 = pokemon1
                nom_pokemon1 = pokemon1['nom']
                niveau_pokemon1 = pokemon1['niveau']
                chemin_image_pokemon1 = f"C:\\Users\\lo\\Desktop\\bbt\\PYTHON\\P_O_O\\pokemon\\images\\{pokemon1['images']}"
                type_dattaque_pokemon1 = pokemon1['type_dattaque']
                point_de_vie_pokemon1 = pokemon1['point_de_vie']
                puissance_dattaque_pokemon1 = pokemon1['puissance_dattaque']
                defense_pokemon1 = pokemon1['defense']

                self.barre_vie_pokemon1 = PokemonBarreDeVie(20, 160, pokemon1)

                texte_nom_pokemon1 = self.font.render(f"Nom: {nom_pokemon1}", True, (0, 0, 0))
                texte_niveau_pokemon1 = self.font.render(f"Niveau: {niveau_pokemon1}", True, (0, 0, 0))
                texte_type_dattaque_pokemon1 = self.font.render(f"Type d'attaque: {type_dattaque_pokemon1}", True, (0, 0, 0))

                self.fenetre.blit(texte_nom_pokemon1, (20, 70))
                self.fenetre.blit(texte_niveau_pokemon1, (20, 100))
                self.fenetre.blit(texte_type_dattaque_pokemon1, (20, 130))

                # Afficher la barre de vie du premier Pokémon
                self.barre_vie_pokemon1.afficher(self.fenetre)

                # Charger et afficher l'image du premier Pokémon sélectionné
                image_pokemon1 = pygame.image.load(chemin_image_pokemon1)
                image_pokemon1 = pygame.transform.scale(image_pokemon1, (100, 100))  # Ajustez la taille selon vos besoins
                self.fenetre.blit(image_pokemon1, (150, 350))  # Déplacer l'image vers le bas

            if pokemon2:
                self.pokemon2 = pokemon2
                nom_pokemon2 = pokemon2['nom']
                niveau_pokemon2 = pokemon2['niveau']
                chemin_image_pokemon2 = f"C:\\Users\\lo\\Desktop\\bbt\\PYTHON\\P_O_O\\pokemon\\images\\{pokemon2['images']}"
                type_dattaque_pokemon2 = pokemon2['type_dattaque']
                point_de_vie_pokemon2 = pokemon2['point_de_vie']
                puissance_dattaque_pokemon2 = pokemon2['puissance_dattaque']
                defense_pokemon2 = pokemon2['defense']

                self.barre_vie_pokemon2 = PokemonBarreDeVie(400, 160, pokemon2)

                texte_nom_pokemon2 = self.font.render(f"Nom: {nom_pokemon2}", True, (0, 0, 0))
                texte_niveau_pokemon2 = self.font.render(f"Niveau: {niveau_pokemon2}", True, (0, 0, 0))
                texte_type_dattaque_pokemon2 = self.font.render(f"Type d'attaque: {type_dattaque_pokemon2}", True, (0, 0, 0))

                self.fenetre.blit(texte_nom_pokemon2, (400, 70))
                self.fenetre.blit(texte_niveau_pokemon2, (400, 100))
                self.fenetre.blit(texte_type_dattaque_pokemon2, (400, 130))

                # Afficher la barre de vie du deuxième Pokémon
                self.barre_vie_pokemon2.afficher(self.fenetre)

                # Charger et afficher l'image du deuxième Pokémon
                image_pokemon2 = pygame.image.load(chemin_image_pokemon2)
                image_pokemon2 = pygame.transform.scale(image_pokemon2, (100, 100))  # Ajustez la taille selon vos besoins
                self.fenetre.blit(image_pokemon2, (550, 350))  # Déplacer l'image vers le bas


            # Effectuer l'attaque du premier Pokémon si son attaque est déclenchée
            if self.pokemon1_attaque and self.pokemon2:
                print(f"{self.pokemon1['nom']} attaque avec {self.pokemon1['type_dattaque']} !")
                self.attaquer(self.pokemon1, self.pokemon2)
                self.barre_vie_pokemon2.afficher(self.fenetre)
                self.pokemon1_attaque = False

                # Vérifier si le deuxième Pokémon a perdu
                if self.pokemon2['point_de_vie'] <= 0:
                    gagnant_surface = self.font.render(f"{self.pokemon1['nom']} a gagné!", True, (0, 255, 0))
                    perdant_surface = self.font.render(f"{self.pokemon2['nom']} a perdu!", True, (255, 0, 0))
                    self.fenetre.blit(gagnant_surface, (20, self.hauteur_fenetre - 50))
                    self.fenetre.blit(perdant_surface, (400, self.hauteur_fenetre - 50))

            # Effectuer l'attaque du deuxième Pokémon si son attaque est déclenchée
            if self.pokemon2_attaque and self.pokemon1:
                print(f"{self.pokemon2['nom']} attaque avec {self.pokemon2['type_dattaque']} !")
                self.attaquer(self.pokemon2, self.pokemon1)
                self.barre_vie_pokemon1.afficher(self.fenetre)
                self.pokemon2_attaque = False

                # Vérifier si le premier Pokémon a perdu
                if self.pokemon1['point_de_vie'] <= 0:
                    gagnant_surface = self.font.render(f"{self.pokemon2['nom']} a gagné!", True, (0, 255, 0))
                    perdant_surface = self.font.render(f"{self.pokemon1['nom']} a perdu!", True, (255, 0, 0))
                    self.fenetre.blit(gagnant_surface, (20, self.hauteur_fenetre - 50))
                    self.fenetre.blit(perdant_surface, (400, self.hauteur_fenetre - 50))

            pygame.display.flip()


if __name__ == "__main__":
    battle_instance = Battle()
    battle_instance.run()
