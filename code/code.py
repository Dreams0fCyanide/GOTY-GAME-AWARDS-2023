import pygame
import pygame_menu
from sys import exit
import tkinter
from tkinter import *
from tkinter import ttk
import os

#Podstawy pygame
pygame.init()

scrn = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
pygame.display.set_caption('Koteczki miłości')


#Zmienne globalne
dane = os.path.dirname(__file__)

ikona = pygame.image.load(os.path.join(dane, '../grafika/catpapiez.png'))
pygame.display.set_icon(ikona)

#menu
imp = pygame.image.load(os.path.join(dane, '../grafika/koteczki.png'))
scrn.blit(imp, (0, 0))


#Główna pętla
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False  

        pygame.display.flip()
        clock.tick(60)

