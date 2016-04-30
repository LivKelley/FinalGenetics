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

size = (640, 480)
class Nitrogene_Graph_Model(size): 
    def __init__(self, size):
        """Initialize within the specialized model""" 
        self.WIDTH = size
        self.left = size[0]
        self.sorter_code(self.code_loader())
    def code_loader (self):
        print pickle.load(open('genes_found.pickle', "wb"))

Nitrogene_Graph_Model()

#     def sorter_code (self, list_of_orfs_imported):

#         self.forward_only_orf = []
#         self.complement_only_orf = []
#         for item in list_of_orfs_imported:
#             if item[6] == 0:
#                 self.forward_only_orf.append(item) 
#             elif item[6] == 1:
#                 self.complement_only_orf.append(item)
# #View - draw functions 

# #Adapted from PolkaDots game from the previous project.
# class Nitrogene_Graph_View (object):
#     def __init__(self, model, forward_only_orf, complement_only_orf, genome):
#         self.screen = pygame.display.set_mode(size)
#         self.model = model 
#         self.threshold = 20 #float(raw_input("Please type a two digit number representing the DNA accuracy threshold percentage."))
#         self.Genome_Bar_Height = 30 
#         self.forward_only_orf = forward_only_orf
#         self.complement_only_orf = complement_only_orf
#         self.genome = genome
#         self.comp_fact = 10 # compression factor

#     def draw(self): 
#         """Draws the gene image onto the windrect(Surface, color, Rect, width=0) -> Rectow."""

#         Mouse_Position = pygame.mouse.get_pos()

#         self.screen.fill(pygame.Color('white'))
#         background = pygame.Surface(screen.get_size()) #This is just making a surface because we have to use blitting to make things show up. 
#         background = background.convert() #This increases speed
#         background.fill((255, 255, 255)) #This needs to match color

#         font = pygame.font.Font(None, 36)
#         text = font.render("Nitrogene Visualization", 1, (0, 0, 0))
#         textpos = text.get_rect()
#         textpos.centerx = 300 
#         background.blit(text, textpos)
#         screen.blit(background, (0,0))

#         #Making the rectangle for the main gene.

#         length = len(self.genome)

#         dna_length_rectangle = pygame.Rect(0,
#                                        self.Genome_Bar_Height + 10,
#                                        length/self.comp_fact, 
#                                        self.Genome_Bar_Height
#                                        )


#         pygame.draw.rect(self.screen, (0,0,100,100), dna_length_rectangle, 0)

#         orf = self.forward_only_orf[0]

#         #Looping through orfs 

#         for orf_num, orf in enumerate(self.forward_only_orf):
#             complement = self.complement_only_orf[orf_num]
#             #Creating the stacking elements that build the bar graph for false values
        

#             orf_rectangle = pygame.Rect('orf_start',
#                                         self.Genome_Bar_Height+10,#(orf_num+1)*(self.Genome_Bar_Height) + orf_num*10
#                                         ('orf_end'- 'orf_start')/self.comp_fact,
#                                         self.Genome_Bar_Height
#                                         )
            
#             if 0 <= 'percent_match' <= self.threshold:

#                 pygame.draw.rect(self.screen, (0, 0, 0, 0), orf_rectangle, 0)
                
#                 #Iterate through the rest of the sequence. 

#             elif 'percent_match'>= self.threshold: 
#                 color_match = (0, 'percent_match', 0, 0) 
#                 pygame.draw.rect(self.screen, color_match, orf_rectangle, 0)

#                 #Scrolling

#             if orf_rectangle.collidepoint(Mouse_Position):
#                 font = pygame.font.Font(None, 26)
#                 text = font.render(("   " + str(int('percent_match')) + " %"), 1, (50, 0, 200))
#                 screen.blit(text, (Mouse_Position))

#             complement_length_rectangle = pygame.Rect(0,
#                                        self.Genome_Bar_Height + 10,
#                                        length/self.comp_fact, 
#                                        self.Genome_Bar_Height
#                                        )


#             pygame.draw.rect(self.screen, (0,0,200, 50), dna_length_rectangle, 0)

#             complement_orf_rectangle = pygame.Rect(complement[4],
#                                         self.Genome_Bar_Height+10,#(orf_num+1)*(self.Genome_Bar_Height) + orf_num*10
#                                         (complement[5]- complement[4])/self.comp_fact,
#                                         self.Genome_Bar_Height
#                                         )

#             if 0 <= complement[3] <= self.threshold:

#                 pygame.draw.rect(self.screen, (0, 0, 0, 0), complement_orf_rectangle, 0)
                
#                 #Iterate through the rest of the sequence. 

#             elif complement[3] >= self.threshold: 
#                 color_match = (0, complement[3], 0, 0) 
#                 pygame.draw.rect(self.screen, color_match, complement_orf_rectangle, 0)

#                 #Scrolling

#             if orf_rectangle.collidepoint(Mouse_Position):
#                 font = pygame.font.Font(None, 26)
#                 text = font.render(("   " + str(int(complement[3])) + " %"), 1, (50, 0, 200))
#                 screen.blit(text, (Mouse_Position))

#             pygame.display.flip()


# #Running the Code (Adapted from the in class brick breaker code.)
# if __name__ == '__main__':

#     pygame.init() 
#     size = (640, 480)
#     model = Nitrogene_Graph_Model(size)  
#     print len(model.forward_only_orf), len(model.complement_only_orf)
#     view = Nitrogene_Graph_View(model, model.forward_only_orf, model.complement_only_orf, pauls_seq)
#     screen = pygame.display.set_mode(size) #This is the surface you want to draw to.
#     #Initialize left and WIDTH 
#     running = True

#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#         view.draw() 
#         time.sleep(.001)