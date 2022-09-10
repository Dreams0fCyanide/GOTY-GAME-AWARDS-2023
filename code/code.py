import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
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
path = os.path.dirname(__file__)
running = True

icon = pygame.image.load(os.path.join(path, '../grafika/catpapiez.png'))
pygame.display.set_icon(icon)

#menu
bcgrnd = pygame.image.load(os.path.join(path, '../grafika/koteczki.png'))
scrn.blit(bcgrnd, (0, 0))

nowa_gra = pygame.Surface((410,79))  # szerokość, wysokość
nowa_gra.set_alpha(0)                # przezroczysty = 0 wypełniony = 255
scrn.blit(nowa_gra, (0,190))    # od lewej i od góry

opcje = pygame.Surface((410,79))  # szerokość, wysokość
opcje.set_alpha(0)                # przezroczysty = 0 wypełniony = 255
scrn.blit(opcje, (0,320))    # od lewej i od góry

wyjdz = pygame.Surface((410,79))  # szerokość, wysokość
wyjdz.set_alpha(0)                # przezroczysty = 0 wypełniony = 255
scrn.blit(wyjdz, (0,450))    # od lewej i od góry

#Główna pętla
while running:
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if wyjdz.collidepoint(pos):
                pygame.quit()
                exit()

        pygame.display.flip()
        clock.tick(60)

