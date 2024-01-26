import pygame
import sys
import json

class Pokemon:
    def __init__(self, nom, niveau, chemin_image, type_dattaque, point_de_vie, puissance_dattaque, defense):
        self.nom = nom
        self.niveau = niveau
        self.chemin_image = chemin_image
        self.type_dattaque = type_dattaque
        self.point_de_vie = point_de_vie
        self.puissance_dattaque = puissance_dattaque
        self.defense = defense

    @classmethod
    def charger_depuis_json(cls, nom_fichier):
        pokemons = []
        with open(nom_fichier, 'r') as f:
            data = json.load(f)
            for pokemon_data in data['pokemons']:
                pokemon = cls(
                    pokemon_data['nom'],
                    pokemon_data['niveau'],
                    pokemon_data['chemin_image'],
                    pokemon_data['type_dattaque'],
                    pokemon_data['point_de_vie'],
                    pokemon_data['puissance_dattaque'],
                    pokemon_data['defense']
                )
                pokemons.append(pokemon)
        return pokemons

class BarreDeVie:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.longueur_barre = 200
        self.largeur_barre = 20

    def afficher(self, surface, vie):
        vie_max = 100
        longueur_vie = int(self.longueur_barre * vie / vie_max)
        pygame.draw.rect(surface, (0, 0, 0), (self.x, self.y, self.longueur_barre, self.largeur_barre), 2)
        if vie > 0:
            pygame.draw.rect(surface, (0, 255, 0), (self.x, self.y, longueur_vie, self.largeur_barre))

class Battle:
    def __init__(self):
        pygame.init()
        self.largeur_fenetre = 800
        self.hauteur_fenetre = 600
        self.fenetre = pygame.display.set_mode((self.largeur_fenetre, self.hauteur_fenetre))
        pygame.display.set_caption("Battle")

        self.pokemons = Pokemon.charger_depuis_json("donnees_pokemon.json")
        self.font = pygame.font.Font(None, 24)

        self.joueur = self.pokemons[0]  # Sélectionnez le premier Pokémon comme joueur
        self.adversaire = self.pokemons[1]  # Sélectionnez le deuxième Pokémon comme adversaire

        self.barre_de_vie_joueur = BarreDeVie(50, 50)
        self.barre_de_vie_adversaire = BarreDeVie(500, 50)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 150 <= event.pos[0] <= 250 and 350 <= event.pos[1] <= 450:
                            # Action du joueur lorsque le Pokémon est cliqué
                            self.attaque(self.joueur, self.adversaire)
                        elif 550 <= event.pos[0] <= 650 and 350 <= event.pos[1] <= 450:
                            # Action de l'adversaire lorsque le Pokémon est cliqué
                            self.attaque(self.adversaire, self.joueur)

            self.fenetre.fill((255, 255, 255))

            self.afficher_pokemon(self.joueur, 150, 350)
            self.afficher_pokemon(self.adversaire, 550, 350)

            pygame.display.flip()

    def attaque(self, attaquant, cible):
        print(f"{attaquant.nom} attaque avec {attaquant.type_dattaque} !")
        # Appliquer les effets spécifiques de l'attaque en fonction du type
        if attaquant.type_dattaque == 'terre':
            cible.point_de_vie -= 5
        elif attaquant.type_dattaque == 'eau':
            cible.point_de_vie -= 15
        elif attaquant.type_dattaque == 'feu':
            cible.point_de_vie -= 20
        elif attaquant.type_dattaque == 'normal':
            cible.point_de_vie -= 10

        # Mettre à jour les barres de vie
        self.mettre_a_jour_barre_de_vie()

    def mettre_a_jour_barre_de_vie(self):
        self.barre_de_vie_joueur.afficher(self.fenetre, self.joueur.point_de_vie)
        self.barre_de_vie_adversaire.afficher(self.fenetre, self.adversaire.point_de_vie)

    def afficher_pokemon(self, pokemon, x, y):
        texte_nom = self.font.render(f"Nom: {pokemon.nom}", True, (0, 0, 0))
        texte_niveau = self.font.render(f"Niveau: {pokemon.niveau}", True, (0, 0, 0))
        texte_type_dattaque = self.font.render(f"Type d'attaque: {pokemon.type_dattaque}", True, (0, 0, 0))

        self.fenetre.blit(texte_nom, (x, y - 50))
        self.fenetre.blit(texte_niveau, (x, y - 20))
        self.fenetre.blit(texte_type_dattaque, (x, y))

        image_pokemon = pygame.image.load(pokemon.chemin_image)
        image_pokemon = pygame.transform.scale(image_pokemon, (100, 100))
        self.fenetre.blit(image_pokemon, (x, y + 100))

if __name__ == "__main__":
    battle_instance = Battle()
    battle_instance.run()
