import pygame 
import pickle
import time 
import sys 
from pickle import dump
from random import choice

#pauls_seq = 'GCCCGGACATTCTACATCTCCGCGAAAACACACACTTTTTCGTCTCCGGCGAAGCTTGGCACGCTCGTTGCAAAACAGGGATCAGCAAGGCGAGGGATGGTTGGCCGAGCAGTTACTGCAAAGGGCAACGTCCGCATCTGAGCCGTGCGACGGTTTTGAACGGAAGAAGGCTGCGCCTCGGCGCAAATCGATCAAGCGGCATTAGGTCAACGGAGAGAAAACATGGCACTTCGGCAAATCGCATTCTACGGCAAGGGCGGCATCGGCAAGTCGACCACCTCGCAGAACACCCTCGCGGCGCTGGTTGAGATGGGTCAGAAGATCCTGATCGTCGGCTGCGACCCCAAGGCGGACTCCACCCGTCTGATCCTCAACACCAAGATGCAGGACACGGTGCTGAGCCTCGCCGCGGAAGCGGGTTCGGTGGAAGACCTCGAACTCGAAGACGTGATGAAGATCGGCTACAAGGGCATCAAGTGCACCGAAGCCGGTGGCCCGGAGCCGGGCGTCGGCTGCGCCGGCCGCGGCGTTATCACCGCGATCAACTTCCTCGAAGAAAACGGCGCCTATGAAGACGTCGACTACGTCTCCTACGACGTGCTCGGCGACGTGGTGTGCGGCGGCTTCGCGATGCCGATCCGTGAAAACAAGGCGCAGGAAATCTACATCGTCATGTCCGGCGAGATGATGGCGCTGTATGCCGCCAACAACATCTCCAAGGGCATTCTGAAGTACGCTTCGTCGGGCGGCGTCCGTCTCGGCGGCCTGATCTGCAACGAGCGCCAGACCGACCGCGAGCTCGACCTCGCCGAAGCGCTGGCCAAGAAGCTGAACTCGAAGCTGATCCACTTCGTGCCGCGCGACAATATCGTGCAGCACGCCGAGCTGCGCCGCCAGACCGTGATCCAGTACGCGCCCGACAGCCAGCAGGCTAAGGAATATCGCGCCCTGGCCAACAAGGTCCATGCCAACTGCGGCAACGGCACCATCCCGACCCCGATCACCATGGAAGAGCTGGAAGAGATGCTGCTCGACTTCGGCATCATGAAGACCGAGGAGCAGCAGCTCGCCGAGCTCGCCGCCAAGGAAGCCGCCAAGGCGGCCGCGTCCGCCTGATCGCATCAGCCAGGCCGGTCGCCTAGCGCGACCGGCCGCCATCCCGGCGGCCCCAGACACGAGGAACAACGATGAGCACCGCAGTCGCAGAATCCCCCGCGGACATCAAGGAACGTAACAAGAAGCTGATCGGCGAAGTCCTGGAGGCCTATCCGGACAAGTCGGCCAAGCGTCGCGCCAAGCATCTCAACACGTACGACGCCGAGAAGGCGGAGTGCTCGGTCAAGTCCAACATCAAGTCGATCCCGGGCGTGATGACGATCCGCGGTTGCGCCTACGCCGGCTCGAAGGGCGTGGTGTGGGGCCCGATCAAGGACATGGTCCACATCAGCCACGGCCCGGTCGGCTGCGGCCAGTATTCGTGGGGTTCGCGCCGCAACTATTACAAGGGAACCACCGGCGTCGACACTTTCGGCACGATGCAGTTCACCTCCGACTTCCAGGAGAAGGACATCGTTTTCGGCGGTGACAAGAAGCTCGGCAAGATCATCGACGAGATCCAGGAGCTGTTCCCGCTCTCCAAGGGCATCTCGGTGCAGTCGGAATGCCCGATCGGTCTGATCGGCGACGACATCGAGGCGGTCTCCAAGGCCAAGTCGAAGCAGTATGACGGCAAGCCGATCATCCCGGTCCGCTGCGAAGGCTTCCGCGGCGTGTCGCAGTCGCTCGGCCACCACATCGCCAACGACGTGATCCGTGACTGGGTGTTCGACAAGGCCGCCGAGAAGAACGCCGGCTTCCAGTCGACCCCCTACGACGTCGCGATCATCGGCGACTACAACATCGGCGGCGATGCCTGGGCCTCGCGCATCCTGCTCGAGGAAATGGGCCTCCGCGTGATCGCGCAGTGGTCCGGCGACGGCACCATCGCGGAGCTGGAGAACACCCCGAAGGCGAAGCTGAACATCCTGCACTGCTACCGCTCGATGAACTACATCACGCGGCACATGGAAGAGAAGTTCGGTATTCCGTGGGTTGAATACAACTTCTTCGGCCCGTCCAAGATCGA'
#Code to determine variables 

#Model

#Changing variables 
#Initializing objects: 

class Nitrogene_Graph_Model(object): 
    def __init__(self, size):
        """Initialize within the specialized model""" 
        self.WIDTH = size
        self.left = size[0]
        self.sorter_code(self.code_loader())
    def code_loader (self):
        return pickle.load(open('genes_foundNoDict.pickle'))

    def sorter_code (self, list_of_orfs_imported):

        self.forward_only_orf = []
        self.complement_only_orf = []
        for item in list_of_orfs_imported:
            if item[6] == 0:
                self.forward_only_orf.append(item) 
            elif item[6] == 1:
                self.complement_only_orf.append(item)
#View - draw functions 

#Adapted from PolkaDots game from the previous project.
class Nitrogene_Graph_View (object):
    def __init__(self, model, forward_only_orf, complement_only_orf):
        self.screen = pygame.display.set_mode(size)
        self.lscreen = pygame.surface.Surface(lsize)

        self.model = model 
        self.threshold = 20 #float(raw_input("Please type a two digit number representing the DNA accuracy threshold percentage."))
        self.Genome_Bar_Height = 10 
        self.forward_only_orf = forward_only_orf
        self.complement_only_orf = complement_only_orf
        self.comp_fact = 10 # compression factor
        self.scroll_y = 0 

    #rectangle_list = []

    def draw(self): 
        """Draws the gene image onto the windrect(Surface, color, Rect, width=0) -> Rectow."""

        for orf_num, orf in enumerate(self.forward_only_orf):
            #Creating the stacking elements that build the bar graph for false values

            #Renaming things for the sake of legibility.

            length = orf[0]
            start = orf[4]
            end = orf[5]
            percent_match = orf[3]

                
            #This code draws the blue bars that represent the length of segments of DNA. 
            dna_length_rectangle = pygame.Rect(0,
                                   (self.Genome_Bar_Height + 10)*(orf_num+1),
                                    length/self.comp_fact,
                                    self.Genome_Bar_Height
                                    )

            pygame.draw.rect(self.lscreen, (0,0,200,100), dna_length_rectangle, 0)

           #Orf - White or green

            orf_rectangle = pygame.Rect(float(start)/self.comp_fact,
                                        (self.Genome_Bar_Height + 10)*(orf_num+1),
                                        float(end- start)/self.comp_fact,
                                        self.Genome_Bar_Height)


            if 0 <= percent_match <= self.threshold:

                pygame.draw.rect(self.lscreen, (150, 150, 150, 150), orf_rectangle, 0)
                
                #Iterate through the rest of the sequence. 

            elif percent_match >= self.threshold: 
                color_match = (0, percent_match, 0, 0) 
                pygame.draw.rect(self.lscreen, color_match, orf_rectangle, 0)

            Mouse_Position = pygame.mouse.get_pos()

            if orf_rectangle.collidepoint(Mouse_Position):
                font = pygame.font.Font(None, 14)
                text = font.render(("   " + str(int(percent_match)) + " %"), 1, (250, 250, 210))
                self.lscreen.blit(text, (Mouse_Position))

    def update(self): 

            self.screen.blit(self.lscreen, (0, self.scroll_y))

            font = pygame.font.Font(None, 36)
            text = font.render("Nitrogene Visualization", 1, (255, 255, 255))
            textpos = text.get_rect()
            self.screen.blit(text, textpos)
            self.screen.blit(self.screen, (0,0))

            pygame.display.flip()

class Nitrogenase_Controller(object):

    def __init__(self, view):
        """Initialize within the specialized model""" 
        self.view = view 

    def Key_Press (self):

        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 4: 
                    self.view.scroll_y = min(self.view.scroll_y + 15, 0)
                if e.button == 5: 
                    self.view.scroll_y = max(self.view.scroll_y - 15, -6000)


#Running the Code (Adapted from the in class brick breaker code.)

if __name__ == '__main__':

    pygame.init() 
    lsize = (600, 6000) #W,L
    size = (600, 640)

    model = Nitrogene_Graph_Model(size)  
    view = Nitrogene_Graph_View(model, model.forward_only_orf, model.complement_only_orf)
    screen = pygame.display.set_mode(size) #This is the surface you want to draw to.
    #Initialize left and WIDTH 
    running = True
    controller = Nitrogenase_Controller(view)
    while running:
        view.draw()
        view.update()
        controller.Key_Press() 
        #view.update() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False 
            time.sleep(.001)

# Get the position of the mouse in the controller
# Pass the mouse position from the controller to view.draw() as a parameter
# Use this position to draw the pop-up with the function you already wrote