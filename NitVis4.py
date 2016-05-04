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
            if 'rev_flag' == 0:
                self.forward_only_orf.append(item) 
            elif 'rev_flag' == 1:
                self.complement_only_orf.append(item)
#View - draw functions 

#Adapted from PolkaDots game from the previous project.
class Nitrogene_Graph_View (object):
    def __init__(self, model, forward_only_orf, complement_only_orf):
        self.screen = pygame.display.set_mode(size)
        self.lscreen = pygame.surface.Surface(lsize)

        self.model = model 
        self.threshold = float(raw_input("Please type a two digit number representing the DNA accuracy threshold percentage."))
        self.Genome_Bar_Height = 10 
        self.forward_only_orf = forward_only_orf
        self.complement_only_orf = complement_only_orf
        self.comp_fact = 30 # compression factor
        self.scroll_y = 0 

    def draw(self): 
        """Draws the gene image onto the windrect(Surface, color, Rect, width=0) -> Rectow."""
        Mouse_Position = pygame.mouse.get_pos()

        print "LENGTH OF ORFS: ", len(self.forward_only_orf)

        print self.forward_only_orf


        for orf_num,orf in enumerate(self.forward_only_orf):
            print "ORF NUM: ", orf_num
            print "ORF: ", orf
            #Creating the stacking elements that build the bar graph for false values

            #Renaming things for the sake of legibility.
                
            #This code draws the blue bars that represent the length of segments of DNA. 
            dna_length_rectangle = pygame.Rect(0,
                                   (self.Genome_Bar_Height + 10)*(orf_num+1),
                                    'length_item'/self.comp_fact,
                                   self.Genome_Bar_Height
                                    )

            pygame.draw.rect(self.lscreen, (0,0,200,100), dna_length_rectangle, 0)

            #Orf - White or green

            orf_rectangle = pygame.Rect(float('start')/self.comp_fact,
                                        (self.Genome_Bar_Height + 10)*(orf_num+1),
                                        float(('end'- 'start')/self.comp_fact),
                                        self.Genome_Bar_Height
                                        )

            if 0 <= 'percent_match' <= self.threshold:

                pygame.draw.rect(self.lscreen, (150, 150, 150, 150), orf_rectangle, 0)
                
                #Iterate through the rest of the sequence. 

            elif 'percent_match'>= self.threshold: 
                color_match = (0, 'percent_match', 0, 0) 
                pygame.draw.rect(self.lscreen, color_match, orf_rectangle, 0)

            #Scrolling

            for 

            Mouse_Position = pygame.mouse.get_pos()

            if orf_rectangle.collidepoint(Mouse_Position):
                font = pygame.font.Font(None, 26)
                text = font.render(("   " + str(int('percent_match')) + " %"), 1, (255, 255, 200))
                screen.blit(text, (Mouse_Position))

            #self.Genome_Bar_Height += 50

            Nitrogenase_Controller(self.Genome_Bar_Height)

            # if orf_rectangle.collidepoint(Mouse_Position):
            #     font = pygame.font.Font(None, 26)
            #     text = font.render(("   " + str(int(complement[3])) + " %"), 1, (50, 0, 200))
            #     lscreen.blit(text, (Mouse_Position))

    def update(self):
        self.screen.blit(self.lscreen, (0, self.scroll_y))

        font = pygame.font.Font(None, 36)
        text = font.render("Nitrogene Visualization", 1, (255, 255, 255))
        textpos = text.get_rect()
        textpos.centerx = 300 
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
                    print "scrolling"
                    self.view.scroll_y = min(self.view.scroll_y + 15, 0)
                if e.button == 5: 
                    print "scrolling"
                    self.view.scroll_y = max(self.view.scroll_y - 15, -6000)


#Running the Code (Adapted from the in class brick breaker code.)
if __name__ == '__main__':

    pygame.init() 
    lsize = (600, 6000) #W,L
    size= (600, 640)

    model = Nitrogene_Graph_Model(size)  
    print len(model.forward_only_orf), len(model.complement_only_orf)
    view = Nitrogene_Graph_View(model, model.forward_only_orf, model.complement_only_orf)
    screen = pygame.display.set_mode(size) #This is the surface you want to draw to.
    #Initialize left and WIDTH 
    running = True
    controller = Nitrogenase_Controller(view)
    view.draw()
    while running:
        controller.Key_Press() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        view.update()
        time.sleep(.001)