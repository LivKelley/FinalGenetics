#This code produces an interactive graph for the nitrogene code using pygame. 

import pygame 
import time 
import sys 
from random import choice
Example_Genome = [(0, 19), (.5, 25), (0, 20)] 
Example_Genome2 = [(0, 15), (.5 , 40), (0, 20), (.9, 10),(.4, 90), (.8, 60),(.7, 30), (.2, 10)]
Genome_List = [Example_Genome, Example_Genome2] #Do we need code that puts each genome list into such a megalist or breaks them out of it (depending on Nitrogene's output?)

#Code to determine variables 

#Model

#Changing variables 
#Initializing objects: 

class Nitrogene_Graph_Model(object): 
    def __init__(self, size):
        """Initialize within the specialized model""" 
        self.WIDTH = size
        self.left = size[0]
        

#View - draw functions 

#Adapted from PolkaDots game from the previous project.
class Nitrogene_Graph_View (object):
    def __init__(self, model):
        self.screen = pygame.display.set_mode(size)
        self.model = model 
        self.threshold = raw_input("Please type a two digit decimal representing the DNA accuracy threshold percentage. Example: .20 would be 20%.")
        self.Genome_Bar_Height = 10 

    def draw(self): 
        """Draws the gene image onto the windrect(Surface, color, Rect, width=0) -> Rectow."""


        Mouse_Position = pygame.mouse.get_pos()

        self.screen.fill(pygame.Color('white'))
        background = pygame.Surface(screen.get_size()) #This is just making a surface because we have to use blitting to make things show up. 
        background = background.convert() #This increases speed
        background.fill((255, 255, 255)) #This needs to match color

        font = pygame.font.Font(None, 36)
        text = font.render("Nitrogene Visualization", 1, (0, 0, 0))
        textpos = text.get_rect()
        textpos.centerx = 300 
        background.blit(text, textpos)
        screen.blit(background, (0,0))


        for genome_num,Genome in enumerate(Genome_List):
            #Creating the stacking elements that build the bar graph for false values
            current = 0

            for gene_num,gene in enumerate(Genome):

                rectangle = pygame.Rect(current, 
                        ((genome_num+1))*(self.Genome_Bar_Height+20),
                        gene[1], 
                        (((genome_num))*self.Genome_Bar_Height +20)
                         )

                if 0 <= gene[0] <= float(self.threshold):

                    pygame.draw.rect(self.screen, (0, 0, 0, 0), rectangle, 0)
                    
                    #Iterate through the rest of the sequence. 

                elif gene[0] >= float(self.threshold): 
                    color_match = (0, gene[0]*255, 0, 0) 
                    pygame.draw.rect(self.screen, color_match, rectangle, 0)

                current += gene[1]

            current = 0

            for gene_num,gene in enumerate(Genome):

                rectangle = pygame.Rect(current, 
                        ((genome_num+1))*(self.Genome_Bar_Height+20),
                        gene[1], 
                        (((genome_num))*self.Genome_Bar_Height +20)
                         )

                if rectangle.collidepoint(Mouse_Position):
                    font = pygame.font.Font(None, 26)
                    text = font.render(("   " + str(gene[0]*100) + " %"), 1, (50, 0, 200))
                    screen.blit(text, (Mouse_Position))
                
                current += gene[1]


        pygame.display.flip()


#class Nitrogene_Controller(): 
    #pygame.mouse.set_cursor(pygame.cursors.arrow)


#Running the Code (Adapted from the in class brick breaker code.)
if __name__ == '__main__':

    pygame.init() 
    size = (640, 480)
    model = Nitrogene_Graph_Model(size)  
    view = Nitrogene_Graph_View(model)
    screen = pygame.display.set_mode(size) #This is the surface you want to draw to.
    #Initialize left and WIDTH 
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        view.draw() 
        time.sleep(.001)