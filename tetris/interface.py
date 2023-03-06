import tkinter as tk
import random

from classeBlock import Block

# Constantes de jeu
GRID_WIDTH = 10
GRID_HEIGHT = 20
BLOCK_SIZE = 30
GAME_SPEED = 500  # en millisecondes

# Formes des blocs
BLOCKS = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # I
    [(0, 0), (1, 0), (0, 1), (1, 1)],  # O
    [(0, 0), (1, 0), (2, 0), (2, 1)],  # L
    [(0, 0), (1, 0), (2, 0), (0, 1)],  # J
    [(0, 0), (1, 0), (1, 1), (2, 1)],  # Z
    [(1, 0), (2, 0), (0, 1), (1, 1)],  # S
    [(1, 0), (0, 1), (1, 1), (2, 1)]   # T
]

# Couleurs des blocs
COLORS = [
    "cyan", "yellow", "orange", "blue", "red", "green", "purple"
]


class TetrisGame:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=GRID_WIDTH * BLOCK_SIZE, height=GRID_HEIGHT * BLOCK_SIZE, bg="black")
        self.canvas.pack()

        # Initialisation de la grille
        self.grid = [[None for x in range(GRID_WIDTH)] for y in range(GRID_HEIGHT)]

        # Variables de jeu
        self.current_block = None
        self.current_shape = None
        self.current_color = None
        self.current_position = None
        self.next_block = None
        self.score = 0

        # Affichage du score
        self.score_label = tk.Label(self.master, text=f"Score: {self.score}", font=("Helvetica", 16))
        self.score_label.pack()

        # Boucle de jeu
        self.master.after(GAME_SPEED, self.game_loop)

    def game_loop(self):
        # Vérification si le jeu est terminé
        if self.check_game_over():
            self.game_over()
            return

        # Création d'un nouveau bloc si nécessaire
        if not self.current_block:
            self.create_new_block()

        # Déplacement du bloc
        self.move_block((0, 1))

        # Affichage du jeu
        self.draw_game()

        # Mise à jour du score
        self.score_label.configure(text=f"Score: {self.score}")

        # Boucle de jeu
        self.master.after(GAME_SPEED, self.game_loop)

    def create_new_block(self):
        # Création d'un nouveau bloc aléatoire
        shape = random.choice(BLOCKS)
        color = random.choice(COLORS)
        position = (GRID_WIDTH // 2 - 2, 0)
        self.current_block = []
        for block in shape:
            x, y = block
            self.current_block.append((x + position[0], y + position[1]))
        self.current_shape = shape
        self.current_color = color
        self.current_position = position

        # Création du bloc suivant
        self.next_block = []
        shape
