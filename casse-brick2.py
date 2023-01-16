class Paddle():


    def __init__(self): # constructeur

        self.w = 120  # attribut longueur du paddle

        self.h = 15   # attribut largeur du paddle

        # la position du paddle avec un objet Pvector

        self.pos = PVector(width/2 - self.w/2, height - 40)

        self.isMovingLeft = False  # booléen pour mouvement à gauche

        self.isMovingRight = False  # idem à droite

        self.stepSize = 20   # pas pour le déplacement

    # méthode premettant l'affichage

    def display(self):

        fill("#ff9664") # couleur de remplissage

        noStroke()  # pas de "bord"

        # affichage du rectangle rect(x,y,longueur, largeur)

        rect(self.pos.x, self.pos.y, self.w, self.h)

    # méthode pour actualiser l'affichage des déplacements

    def update(self):

        if self.isMovingLeft:

            self.move(-self.stepSize)

        elif self.isMovingRight:

            self.move(self.stepSize)

     # méthode qui gère le déplacement

    def move(self, step):

        self.pos.x +=step

    # méthode qui gère les collisions avec les bords

    def checkEdges(self):

        if self.pos.x <= 0:

            self.pos.x = 0

        elif self.pos.x + self.w >= width:

            self.pos.x = width - self.w

  --------------------------------------------------------------------------------


from Paddle import Paddle #import de la classe Paddle


def setup():

    global paddle # on déclare la variable paddle comme globale

    size(605,400)

    paddle = Paddle() # on crée l'objet paddle



def draw():

    background(0,0,0)

    #appel des méthodes pour le paddle

    paddle.display()

    paddle.checkEdges()

    paddle.update()


#détection des mouvements touches a et d

def keyPressed():

    if key == "a" or key == "A":

        paddle.isMovingLeft = True

    elif key == "d" or key == "D":

        paddle.isMovingRight = True

#annulation des mouvements quand on relâche la touche

def keyReleased():

    paddle.isMovingRight = False

    paddle.isMovingLeft = False


 -------------------------------------------------------------------------------

class Ball():


    def __init__(self):# le constructeur

        self.r = 10 #attribut rayon

        self.vel = PVector(1, 1)*4 # attribut vitesse

        self.dir = PVector(1, 1) # attribut direction

        self.pos = PVector(width/2, height/2) # attribut position



    # méthode pour l'actualisation de la position

    def update(self):

        self.pos.x += self.vel.x*self.dir.x

        self.pos.y += self.vel.y*self.dir.y



    # méthode pour afficher la balle ellipse(x,y,diamètre horizontal, diamètre vertical)

    def display(self):

        fill("#ffff64")

        noStroke()

        ellipse(self.pos.x, self.pos.y, self.r*2, self.r*2)



    #méthode pour les collision avec les bords

    def checkEdges(self):

        # bord droit

        if (self.pos.x > width - self.r and self.dir.x > 0):

            self.dir.x *= -1 # on change le signe de la direction

        # bord gauche

        if (self.pos.x < self.r and self.dir.x < 0):

            self.dir.x *= -1

        # bord haut

    if (self.pos.y < self.r and self.dir.y < 0):

            self.dir.y *= -1

        # bord bas

        if (self.pos.y > height - self.r and self.dir.y > 0):

            self.dir.y *= -1



    # méthode pour détecter la collision avec le paddle

    def meets(self, paddle):

        if (self.pos.y < paddle.pos.y and

            self.pos.y > paddle.pos.y - self.r and

            self.pos.x > paddle.pos.x - self.r and

            self.pos.x < paddle.pos.x + paddle.w + self.r):

            return True

        else:

            return False

--------------------------------------------------------------

from Paddle import Paddle #imp
from Ball import Ball
playingGame
= False

def draw)
global playingGame
background (0,0, 0)
#appel des méthodes pour le paddle
paddle.display()
if playingGame:
paddle. checkEdges()
paddle.update()
#
appel des méthodes pour la balle
ball.display()
if playingGame:
ball. checkEdges()
ball.update()
if (ball.meets (paddle)) :
if (ball.dir.y >
0)
ball.dir. v *= -1

def mousePressed():
global playingGame
playingGame =True

------------------------------------------------------------

# coding=utf-8

class Brick():
    #attribut de classe un dictionnaire de couleurs
    COLORS = {1: "#64ff96", 2: "#ff6496", 3: "#9664ff"}

    def __init__(self, x, y, hits):# le constructeur
        self.w = 75 # attribut longueur
        self.h = 20 # attreibut largeur
        self.pos = PVector(x, y) # attribut position
        self.hits = hits #attribut clé pour la couleur
        self.col = Brick.COLORS[hits] # la couleur

    # méthode pour afficher la brique
    def display(self):
        fill(self.col)
        stroke("#ffffff") # couleur du bord
        strokeWeight(2)# épaisseur des bords
        rect(self.pos.x, self.pos.y, self.w, self.h)

def meets(self,brick) :
if (self.pos.y < brick.pos.y+ brick.h and
self.pos.y > brick.pos.y
self.r and
self.pos.x > brick.pos. x
self.r and
self.pos. x
< brick.pos.x + brick.w + self.r) :
return True
else:
return False

----------------------------------------------------------

bricks=[]
#création de la liste

def setup):
global paddle, ball # on déclare les variables paddle et
size (605,400)
paddle = Paddle) # on crée l'obiet paddle
ball = Ball(
# appel de la fonction addBrick pour ajouter les briques
for x in range (5, width
- 80, 75):
addBrick(x + 37.5, 50, 3)
addBrick(x + 37.5,70, 2)
addBrick(x + 37.5,90, 1)

# fonction créant et stockant les briques dans la liste
def addBrick(x, y, hits) :
brick = Brick(x, y, hits)
bricks.append (brick)


for i
in range (len(bricks)):
bricks[i].display()
for
i
in range(len (bricks) -1,
-
if (ball.meets (bricks[i]))
bricks.pop(i)
#del bricks[i]
ball.dir.y*=-1
