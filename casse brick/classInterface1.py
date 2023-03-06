from tkinter import Tk, Label, Button,Frame,Canvas, Pack, PhotoImage
from classRaquette import Raquette
from classBrick import Brick
from classBalle import Balle
from math import cos,pi,sin

#application de tkinter a partir des classes

class Interface :
    def __init__(self,nom_du_jeu) :

        #création d'une fenêtre graphique
        self.monjeu = Tk() 
        #paramètres de la fenêtre
        self.monjeu.title(nom_du_jeu)
        self.monjeu.config(bg='black')
        self.monjeu.geometry("900x900")

        #canvas de jeu
        self.hauteur = 700
        self.largeur = 700
        self.jeu = Canvas(self.monjeu,width=700,height=700)
        #self.bg = "#000000"
        self.jeu.configure(bg="grey")


        #canvas contenant les boutons
        self.canvas_boutons = Canvas(self.monjeu,width=100 ,height=100)
        self.canvas_boutons.config(bg='black')
        
        #création du widget bouton
        self.buttonQuitt  = Button (self.canvas_boutons, text="QUITTER", fg = 'blue',activebackground="blue", activeforeground="white", command = self.monjeu.destroy, cursor="cross")
        self.jeu.create_rectangle(0,678,492,700,fill='grey') #Pour le score

        self.jeu.create_text(415,685,text='Score: ')
        self.tscore =  self.jeu.create_text(460,685,text='0')

        #sens mouvement
        self.sens = -1
        self.direction = -1

        #score et point
        



    def crea_Raquette(self):
        self.RaquetteR = Raquette()
        self.hauteurR = (self.hauteur*self.RaquetteR.get_positionY())/100
        self.largeurR = (self.largeur*self.RaquetteR.get_positionX())/100
        self.image_raquette = PhotoImage(file="photo/raquette.png")
        self.raquette = self.jeu.create_image(self.largeurR,self.hauteurR,image=self.image_raquette)
        

    def deplacer_Raquette(self,event):
        """Methode pour déplacer la raquette avec les touches a & z"""
        #Gestion de l'evnmt fleche gauche et droite sur la zone graphique
        touche = event.keysym

        if (touche == 'Right') and (self.jeu.coords(self.raquette)[0] < self.largeur-40) :
            self.dX = 20
            self.largeurR += self.dX
            #on dessine la raquette à sa nouvelle position
            self.jeu.move(self.raquette,self.dX,0)

        if (touche == 'Left') and (self.jeu.coords(self.raquette)[0] > 40) :
            self.dX = -20
            self.largeurR += self.dX
            #on dessine la raquette à sa nouvelle position
            self.jeu.move(self.raquette,self.dX,0)

        
    def mouv_raquette(self):
        """Méthode mouvement de la raquette appel de la methode de deplacement en fonction de la touche"""
        self.monjeu.bind("<Right>", self.deplacer_Raquette)
        self.monjeu.bind("<Left>", self.deplacer_Raquette)

    def crea_brick(self):
        self.brick=[]
        self.bricks=[]
        self.coordbrick = [] 
        self.xbrick = Brick(15,80).get_positionX() 
        self.ybrick = Brick(15,80).get_positionY() 
        while self.xbrick<660:
            self.brick.append(self.jeu.create_rectangle(self.xbrick,self.ybrick,self.xbrick+50,self.ybrick+30,fill="orange"))
            self.coordbrick.append([self.xbrick,self.ybrick])
            self.bricks.append([Brick(self.xbrick,self.ybrick)])
            self.ybrick+=30
            if self.ybrick>=160:
                self.xbrick+=50
                self.ybrick = 30


    def crea_balle(self):
        """fonction création de la balle au milieu"""
        self.balleB = Balle(50,50)
        (self.xb,self.yb)=self.jeu.coords(self.raquette)
        #self.balleB = Balle(self.xb,self.yb)
        self.hauteurB = (self.hauteur*self.balleB.get_positionY())/100
        self.largeurB = (self.largeur*self.balleB.get_positionX())/100
        self.coordballe=[self.largeurB,self.hauteurB]
        #self.image_balle = PhotoImage(file="photo/balle.png")
        #self.balle = self.jeu.create_image(self.largeurR,self.hauteurR,image=self.image_balle)
        self.balle = self.jeu.create_rectangle(self.largeurB,self.hauteurB-20,self.largeurB+5,self.hauteurB-15,outline='black',fill='orange')


    def deplacement_balle(self):
        #On modifie les coordonnées de la balle en fonction des précedentes
        self.x = self.coordballe[0]
        self.y = self.coordballe[1]
        #(self.x,self.y)= self.jeu.coords(self.balleB)
        '''self.y = self.y*self.sens+ sin(pi/3)*self.sens
        self.x =self.x*self.direction+ (cos(pi/3))*self.direction'''
        self.y = self.y+ sin(pi/3)*self.sens
        self.x =self.x+ (cos(pi/3))*self.direction
        self.coordballe[1]=self.y
        self.coordballe[0]=self.x

        self.jeu.coords(self.balle,self.x,self.y,self.x+10,self.y+10)
        self.jeu.after(30, self.deplacement_balle)
        


    def destroy_bricks(self,bricks, ball):
        for brick in bricks:
            if isinstance(brick, Brick) and brick.collides_with(ball):
                bricks.remove(brick)
                return True


    def destruction_brick(self):
        i=0
        while i < len(self.bricks):
            if self.destroy_bricks(self.bricks,self.balleB):
                self.jeu.delete(self.brick[i])
                del self.brick[i]
                del self.coordbrick[i]
                self.sens+= -1
            i+=1

          



    '''def rebondissement_raquette(self):  
        if self.jeu.coords(self.raquette)[0]-2 <= self.x <= self.jeu.coords(self.raquette)[0]+52 and self.jeu.coords(self.raquette)[1]-2 <= self.y <= self.jeu.coords(self.raquette)[1]+10:
            self.direction += -1
            self.sens += -1'''




    def lancement(self):
        """fonction appelée dans le fichier jouer, permettant le lancement de l'interface"""
        self.canvas_boutons.pack(side="left")
        self.buttonQuitt.pack(side='bottom', padx=30, pady=30)
        self.jeu.pack()
        #affichage des objets
        self.crea_Raquette()
        self.crea_brick()
        self.mouv_raquette()
        self.crea_balle()
        self.deplacement_balle()
        self.destruction_brick()
        #self.rebondissement_raquette()

        
        #affichage de la fenetre
        self.monjeu.mainloop()

play = Interface("Casse Brick Laetitia Montbarbon")
play.lancement()

