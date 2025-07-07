#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame   #0__Importando o pygame
from code.menu import Menu  #0__ Importando Menu.py, para que ele consiga ser utilizado na while true


class Game:
    def __init__(self):
        pygame.init()  # Ativando o pygame
        self.window = pygame.display.set_mode(size=(600, 480))  # Definir o tamanho da tela

    def run(self):
        while True: #Fazendo com que a janela abrá, antes não estava respondendo.
            menu = Menu(self.window)
            menu.run()
            pass


            # Check for all events
            # for event in pygame.event.get():
            #   if event.type == pygame.QUIT:
            #        pygame.quit() #Close Window
            #           quit() #end pygame

