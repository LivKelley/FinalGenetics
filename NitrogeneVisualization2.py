#This code produces an interactive graph for the nitrogene code using pygame. 

import pygame 
import pickle
import time 
import sys 
from pickle import dump
from random import choice

pauls_seq = 'GCCCGGACATTCTACATCTCCGCGAAAACACACACTTTTTCGTCTCCGGCGAAGCTTGGCACGCTCGTTGCAAAACAGGGATCAGCAAGGCGAGGGATGGTTGGCCGAGCAGTTACTGCAAAGGGCAACGTCCGCATCTGAGCCGTGCGACGGTTTTGAACGGAAGAAGGCTGCGCCTCGGCGCAAATCGATCAAGCGGCATTAGGTCAACGGAGAGAAAACATGGCACTTCGGCAAATCGCATTCTACGGCAAGGGCGGCATCGGCAAGTCGACCACCTCGCAGAACACCCTCGCGGCGCTGGTTGAGATGGGTCAGAAGATCCTGATCGTCGGCTGCGACCCCAAGGCGGACTCCACCCGTCTGATCCTCAACACCAAGATGCAGGACACGGTGCTGAGCCTCGCCGCGGAAGCGGGTTCGGTGGAAGACCTCGAACTCGAAGACGTGATGAAGATCGGCTACAAGGGCATCAAGTGCACCGAAGCCGGTGGCCCGGAGCCGGGCGTCGGCTGCGCCGGCCGCGGCGTTATCACCGCGATCAACTTCCTCGAAGAAAACGGCGCCTATGAAGACGTCGACTACGTCTCCTACGACGTGCTCGGCGACGTGGTGTGCGGCGGCTTCGCGATGCCGATCCGTGAAAACAAGGCGCAGGAAATCTACATCGTCATGTCCGGCGAGATGATGGCGCTGTATGCCGCCAACAACATCTCCAAGGGCATTCTGAAGTACGCTTCGTCGGGCGGCGTCCGTCTCGGCGGCCTGATCTGCAACGAGCGCCAGACCGACCGCGAGCTCGACCTCGCCGAAGCGCTGGCCAAGAAGCTGAACTCGAAGCTGATCCACTTCGTGCCGCGCGACAATATCGTGCAGCACGCCGAGCTGCGCCGCCAGACCGTGATCCAGTACGCGCCCGACAGCCAGCAGGCTAAGGAATATCGCGCCCTGGCCAACAAGGTCCATGCCAACTGCGGCAACGGCACCATCCCGACCCCGATCACCATGGAAGAGCTGGAAGAGATGCTGCTCGACTTCGGCATCATGAAGACCGAGGAGCAGCAGCTCGCCGAGCTCGCCGCCAAGGAAGCCGCCAAGGCGGCCGCGTCCGCCTGATCGCATCAGCCAGGCCGGTCGCCTAGCGCGACCGGCCGCCATCCCGGCGGCCCCAGACACGAGGAACAACGATGAGCACCGCAGTCGCAGAATCCCCCGCGGACATCAAGGAACGTAACAAGAAGCTGATCGGCGAAGTCCTGGAGGCCTATCCGGACAAGTCGGCCAAGCGTCGCGCCAAGCATCTCAACACGTACGACGCCGAGAAGGCGGAGTGCTCGGTCAAGTCCAACATCAAGTCGATCCCGGGCGTGATGACGATCCGCGGTTGCGCCTACGCCGGCTCGAAGGGCGTGGTGTGGGGCCCGATCAAGGACATGGTCCACATCAGCCACGGCCCGGTCGGCTGCGGCCAGTATTCGTGGGGTTCGCGCCGCAACTATTACAAGGGAACCACCGGCGTCGACACTTTCGGCACGATGCAGTTCACCTCCGACTTCCAGGAGAAGGACATCGTTTTCGGCGGTGACAAGAAGCTCGGCAAGATCATCGACGAGATCCAGGAGCTGTTCCCGCTCTCCAAGGGCATCTCGGTGCAGTCGGAATGCCCGATCGGTCTGATCGGCGACGACATCGAGGCGGTCTCCAAGGCCAAGTCGAAGCAGTATGACGGCAAGCCGATCATCCCGGTCCGCTGCGAAGGCTTCCGCGGCGTGTCGCAGTCGCTCGGCCACCACATCGCCAACGACGTGATCCGTGACTGGGTGTTCGACAAGGCCGCCGAGAAGAACGCCGGCTTCCAGTCGACCCCCTACGACGTCGCGATCATCGGCGACTACAACATCGGCGGCGATGCCTGGGCCTCGCGCATCCTGCTCGAGGAAATGGGCCTCCGCGTGATCGCGCAGTGGTCCGGCGACGGCACCATCGCGGAGCTGGAGAACACCCCGAAGGCGAAGCTGAACATCCTGCACTGCTACCGCTCGATGAACTACATCACGCGGCACATGGAAGAGAAGTTCGGTATTCCGTGGGTTGAATACAACTTCTTCGGCCCGTCCAAGATCGA'

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
        return pickle.load(open('genes_found.pickle'))

    def sorter_code (self, list_of_orfs_imported):

        self.forward_only_orf = []
        complement_only_orf = []
        for item in list_of_orfs_imported:
            if item[6] == 0:
                self.forward_only_orf.append(item) 
            elif item[6] == 1:
                complement_only_orf.append(item)
#View - draw functions 

#Adapted from PolkaDots game from the previous project.
class Nitrogene_Graph_View (object):
    def __init__(self, model, forward_only_orf, genome):
        self.screen = pygame.display.set_mode(size)
        self.model = model 
        self.threshold = raw_input("Please type a two digit decimal representing the DNA accuracy threshold percentage. Example: .20 would be 20%.")
        self.Genome_Bar_Height = 30 
        self.forward_only_orf = forward_only_orf
        self.genome = genome
        self.comp_fact = 10 # compression factor

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

        #Making the rectangle for the main gene.

        length = len(self.genome)

        length_rectangle = pygame.Rect(1,
                                       self.Genome_Bar_Height + 10,
                                       length/self.comp_fact, 
                                       self.Genome_Bar_Height
                                       )


        pygame.draw.rect(self.screen, (255,0,0,0), length_rectangle, 0)

        #Looping through orfs 

        for orf_num, orf in enumerate(self.forward_only_orf):
            #Creating the stacking elements that build the bar graph for false values
            current_orf = 0

            #Drawing the orf 

            orf_rectangle = pygame.Rect(orf[4],
                                        (orf_num+1)*(self.Genome_Bar_Height) + orf_num*10,
                                        orf[5]/self.comp_fact- orf[4]/self.comp_fact,
                                        self.Genome_Bar_Height
                                        )
            # pygame.draw.rect(self.screen, (100,0,0,0), orf_rectangle, 0)

            #Drawing nitrogenases on the orf  

            #nitrogenase_rectangle = pygame.Rect(current_orf- orf[4], 
                    #(orf_num+1)*(self.Genome_Bar_Height) + orf_num * 10,
                    #orf[1], 
                    #(self.Genome_Bar_Height)
                     #)

            if 0 <= orf[2] <= float(self.threshold):

                pygame.draw.rect(self.screen, (0, 0, 0, 0), orf_rectangle, 0)
                
                #Iterate through the rest of the sequence. 

            elif orf[2] >= float(self.threshold): 
                color_match = (0, orf[3], 0, 0) 
                pygame.draw.rect(self.screen, color_match, orf_rectangle, 0)

            current_orf += orf[0] + 1 

            current = 0

            #Scrolling

            for orf_num, orf in (enumerate(self.forward_only_orf)):

                orf_rectangle = pygame.Rect(current_orf,
                                        (orf_num+1)*(self.Genome_Bar_Height) + orf_num*10,
                                        orf[5]/self.comp_fact-orf[4]/self.comp_fact,
                                        self.Genome_Bar_Height
                                        )
                pygame.draw.rect(self.screen, (255,0,0,0), orf_rectangle, 0)

                if orf_rectangle.collidepoint(Mouse_Position):
                    font = pygame.font.Font(None, 26)
                    text = font.render(("   " + str(orf[2]*100) + " %"), 1, (50, 0, 200))
                    screen.blit(text, (Mouse_Position))

                #Drawing nitrogenases on the general 

                # nitrogenase_rectangle = pygame.Rect(current_orf- orf[4], 
                #         (orf_num+1)*(self.Genome_Bar_Height) + orf_num * 10,
                #         orf[1], 
                #         (self.Genome_Bar_Height)
                #          )

                # if nitrogenase_rectangle.collidepoint(Mouse_Position):
                #     font = pygame.font.Font(None, 26)
                #     text = font.render(("   " + str(orf[2]*100) + " %"), 1, (50, 0, 200))
                #     screen.blit(text, (Mouse_Position))
                
                #     current_orf += orf[0]+1


        pygame.display.flip()

#Running the Code (Adapted from the in class brick breaker code.)
if __name__ == '__main__':

    pygame.init() 
    size = (640, 480)
    model = Nitrogene_Graph_Model(size)  
    view = Nitrogene_Graph_View(model, model.forward_only_orf, pauls_seq)
    screen = pygame.display.set_mode(size) #This is the surface you want to draw to.
    #Initialize left and WIDTH 
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        view.draw() 
        time.sleep(.001)