#This code produces an interactive graph for the nitrogene code using pygame. 

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
        return pickle.load(open('genes_found.pickle'))

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
        self.model = model 
        self.threshold = 20 #float(raw_input("Please type a two digit number representing the DNA accuracy threshold percentage."))
        self.Genome_Bar_Height = 30 
        self.forward_only_orf = forward_only_orf
        self.complement_only_orf = complement_only_orf
        self.comp_fact = 10 # compression factor


    def draw(self): 
        """Draws the gene image onto the windrect(Surface, color, Rect, width=0) -> Rectow."""
        print 'Liv1'
        Mouse_Position = pygame.mouse.get_pos()

        self.screen.fill(pygame.Color('white'))
        background = pygame.Surface(screen.get_size()) #This is just making a surface because we have to use blitting to make things show up. 
        background = background.convert() #This increases speed
        background.fill((255, 255, 255, 255)) #This needs to match color

        font = pygame.font.Font(None, 36)
        text = font.render("Nitrogene Visualization", 1, (0, 0, 0))
        textpos = text.get_rect()
        textpos.centerx = 300 
        background.blit(text, textpos)
        screen.blit(background, (0,0))

        pygame.draw.rect(self.screen, (0, 0, 100, 100), (size[0] +10, size[1]-11, 10, size[1]-21), 0) 

        # font = pygame.font.Font(None, 36)
        # text = font.render("Key", 1, (0, 0, 0))
        # textpos = text.get_rect()
        # textpos.centerx = 300 
        # background.blit(text, textpos)
        # screen.blit(background, (0,0))
        # #Making the rectangle for the main gene.

        # pygame.draw.rect(self.screen, (0, 0, 100, 100), (size[0] +1, size[1]-13, 5, size[1]-14), 0)
        # pygame.draw.rect(self.screen, (0, 0, 200, 50), (size[0] +1, size[1]-17, 5, size[1]-18), 0) 
        # pygame.draw.rect(self.screen, (0, 250, 0, 0), (size[0] +1, size[1]-15, 5, size[1]-16), 0) 
        # pygame.draw.rect(self.screen, (0, 0, 0, 0), (size[0] +1, size[1]-19, 5, size[1]-20), 0) 

        # # font = pygame.font.Font(None, 36)
        # # text = font.render("Forward Short", 1, (0, 0, 0))
        # # textpos = text.get_rect()
        # # textpos.centerx = 300 
        # # background.blit(text, textpos)
        # # screen.blit(background, (0,0))

        # # font = pygame.font.Font(None, 36)
        # # text = font.render("Complement Short", 1, (0, 0, 0))
        # # textpos = text.get_rect()
        # # textpos.centerx = 300 
        # # background.blit(text, textpos)
        # # screen.blit(background, (0,0))

        # # font = pygame.font.Font(None, 36)
        # # text = font.render("Match", 1, (0, 0, 0))
        # # textpos = text.get_rect()
        # # textpos.centerx = 300 
        # # background.blit(text, textpos)
        # # screen.blit(background, (0,0))


        # # font = pygame.font.Font(None, 36)
        # # text = font.render("Non-Match", 1, (0, 0, 0))
        # # textpos = text.get_rect()
        # # textpos.centerx = 300 
        # # background.blit(text, textpos)
        # # screen.blit(background, (0,0))


        #Looping through orfs 

        for orf_num, orf in enumerate(self.forward_only_orf):
            #Creating the stacking elements that build the bar graph for false values
            length = orf[0]

            dna_length_rectangle = pygame.Rect(0,
                                    self.Genome_Bar_Height + 10,
                                    length/self.comp_fact, 
                                    self.Genome_Bar_Height
                                       )


            pygame.draw.rect(self.screen, (0,0,100,100), dna_length_rectangle, 0)

            orf = self.forward_only_orf[0]
            orf_rectangle = pygame.Rect(orf[4],
                                        self.Genome_Bar_Height+10,#(orf_num+1)*(self.Genome_Bar_Height) + orf_num*10
                                        (orf[5] - orf[4])/self.comp_fact,
                                        self.Genome_Bar_Height
                                        )
    
            if 0 <= orf[3] <= self.threshold:

                pygame.draw.rect(self.screen, (0, 0, 0, 0), orf_rectangle, 0)
                
                #Iterate through the rest of the sequence. 

            elif orf[3] >= self.threshold: 
                color_match = (0, orf[3], 0, 0) 
                pygame.draw.rect(self.screen, color_match, orf_rectangle, 0)

                #Scrolling

            if orf_rectangle.collidepoint(Mouse_Position):
                font = pygame.font.Font(None, 26)
                text = font.render(("   " + str(int(orf[3])) + " %"), 1, (50, 0, 200))
                screen.blit(text, (Mouse_Position))

            Nitrogenase_Controller(self.Genome_Bar_Height)

            
            for complement_num, complement in enumerate(self. complement_only_orf): 
                complement_length = complement[0]

                complement_length_rectangle = pygame.Rect(0,
                                       self.Genome_Bar_Height + 10,
                                       complement_length/self.comp_fact, 
                                       self.Genome_Bar_Height
                                       )


                pygame.draw.rect(self.screen, (0,0,200, 50), complement_length_rectangle, 0)
                
                complement_orf_rectangle = pygame.Rect(complement[4],
                                        self.Genome_Bar_Height+10,#(orf_num+1)*(self.Genome_Bar_Height) + orf_num*10
                                        (complement[5]- complement[4])/self.comp_fact,
                                        self.Genome_Bar_Height
                                        )


                if 0 <= complement[3] <= self.threshold:

                    pygame.draw.rect(self.screen, (0, 0, 0, 0), complement_orf_rectangle, 0)
                    
                    #Iterate through the rest of the sequence. 

                elif complement[3] >= self.threshold: 
                    color_match = (0, complement[3], 0, 0) 
                    pygame.draw.rect(self.screen, color_match, complement_orf_rectangle, 0)

                    #Scrolling

                if orf_rectangle.collidepoint(Mouse_Position):
                    font = pygame.font.Font(None, 26)
                    text = font.render(("   " + str(int(complement[3])) + " %"), 1, (50, 0, 200))
                    screen.blit(text, (Mouse_Position))
                   
        pygame.display.flip()


class Nitrogenase_Controller(object): 
    def __init__(self, view):
        """Initialize within the specialized model""" 
        self.view = view 

    def Key_Press (self): 

        if pygame.key.get_pressed()[pygame.K_UP]: 
            self.view.Genome_Bar_Height += 20 

        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.view.Genome_Bar_Height -= 20  


#Running the Code (Adapted from the in class brick breaker code.)
if __name__ == '__main__':

    pygame.init() 
    size = (640, 480)
    model = Nitrogene_Graph_Model(size)  
    print len(model.forward_only_orf), len(model.complement_only_orf)
    view = Nitrogene_Graph_View(model, model.forward_only_orf, model.complement_only_orf)
    screen = pygame.display.set_mode(size) #This is the surface you want to draw to.
    #Initialize left and WIDTH 
    running = True
    controller = Nitrogenase_Controller(view)
    while running:
        controller.Key_Press() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        view.draw() 
        time.sleep(.001)