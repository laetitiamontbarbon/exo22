class Block:
    def __init__(self, game, position, shape, color):
        self.game = game
        self.position = position
        self.shape = shape
        self.color = color

    def move(self, direction):
        new_position = (self.position[0] + direction[0], self.position[1] + direction[1])
        if not self.check_collision(new_position, self.shape):
            self.position = new_position

    def rotate(self):
        new_shape = []
        for block in self.shape:
            x, y = block
            new_x = self.position[0] + y - self.shape[0][1]
            new_y = self.position[1] - x + self.shape[0][0]
            new_shape.append((new_x, new_y))
        if not self.check_collision(self.position, new_shape):
            self.shape = new_shape

    def check_collision(self, position, shape):
        for block in shape:
            x, y = block
            new_x, new_y = x + position[0], y + position[1]
            if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT or self.game.grid[new_y][new_x]:
                return True
        return False

    def draw(self):
        for block in self.shape:
            x, y = block
            new_x, new_y = (self.position[0] + x) * BLOCK_SIZE, (self.position[1] + y) * BLOCK_SIZE
            self.game.canvas.create_rectangle(new_x, new_y, new_x + BLOCK_SIZE, new_y + BLOCK_SIZE, fill=self.color)
