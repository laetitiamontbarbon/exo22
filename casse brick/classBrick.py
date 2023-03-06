class Brick:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 30

    def get_positionX(self):
        return self.x

    def get_positionY(self):
        return self.y

    def collides_with(self, balle):
        if balle.x + balle.width > self.x and \
           balle.x - balle.width < self.x + self.width and \
           balle.y + balle.height > self.y and \
           balle.y - balle.height < self.y + self.height:
            return True
        else:
            return False