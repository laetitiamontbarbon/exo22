class Balle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 5
        self.height = 3

    def get_positionX(self):
        return self.x

    def get_positionY(self):
        return self.y

    def collides_with(self, brick):
        if self.x + self.width > brick.x and \
           self.x - self.width < brick.x + brick.width and \
           self.y + self.height > brick.y and \
           self.y - self.height < brick.y + brick.height:
            return True
        else:
            return False





