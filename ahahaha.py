import tkinter as tk
import random

# Game constants
WIDTH = 400
HEIGHT = 400
SPEED = 100
SEG_SIZE = 20

class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(width=WIDTH, height=HEIGHT, background="black", highlightthickness=0)

        # Initialize game variables
        self.segments = [(100, 100), (80, 100), (60, 100)]
        self.direction = "Right"
        self.food_position = self._create_food()
        self.score = 0

        # Bind key events
        self.bind_all("<Key>", self._on_key_press)

        # Set up game loop
        self.after(SPEED, self._move)

    def _create_food(self):
        x = random.randint(0, (WIDTH - SEG_SIZE) // SEG_SIZE) * SEG_SIZE
        y = random.randint(0, (HEIGHT - SEG_SIZE) // SEG_SIZE) * SEG_SIZE
        self.create_oval(x, y, x + SEG_SIZE, y + SEG_SIZE, outline="white", fill="white")
        return (x, y)

    def _move(self):
        # Check for collision with food
        if self.segments[0] == self.food_position:
            self.food_position = self._create_food()
            self.score += 1
            self.create_text(50, 12, text=f"Score: {self.score}", fill="white", tag="score")

        # Move snake
        head_x, head_y = self.segments[0]
        if self.direction == "Right":
            new_head = (head_x + SEG_SIZE, head_y)
        elif self.direction == "Left":
            new_head = (head_x - SEG_SIZE, head_y)
        elif self.direction == "Up":
            new_head = (head_x, head_y - SEG_SIZE)
        elif self.direction == "Down":
            new_head = (head_x, head_y + SEG_SIZE)
        self.segments = [new_head] + self.segments[:-1]

        # Check for collision with walls or self
        if (new_head in self.segments[1:]) or \
           (new_head[0] < 0) or (new_head[0] >= WIDTH) or \
           (new_head[1] < 0) or (new_head[1] >= HEIGHT):
            self.create_text(WIDTH / 2, HEIGHT / 2, text="GAME OVER!", fill="white", font=("TkDefaultFont", 28))
            return

        # Clear canvas and redraw segments
        self.delete(tk.ALL)
        self.create_oval(self.food_position[0], self.food_position[1],
                          self.food_position[0] + SEG_SIZE, self.food_position[1] + SEG_SIZE,
                          outline="white", fill="white")
        for x, y in self.segments:
            self.create_rectangle(x, y, x + SEG_SIZE, y + SEG_SIZE, outline="white", fill="white")

        # Schedule next move
        self.after(SPEED, self._move)

    def _on_key_press(self, event):
        new_direction = event.keysym
        if new_direction in ["Up", "Down", "Left", "Right"]:
            opposite_directions = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
            if new_direction != opposite_directions.get(self.direction):
                self.direction = new_direction

# Create game window and start game
root = tk.Tk()
root.title("Snake")
root
