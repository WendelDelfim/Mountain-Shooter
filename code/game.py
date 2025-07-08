#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame   #0__Importando o pygame

from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.menu import Menu  #0__ Importando Menu.py, para que ele consiga ser utilizado na while true


class Game:
    def __init__(self):
        pygame.init()  # Ativando o pygame
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # Definir o tamanho da tela

    def run(self):

        while True: #Fazendo com que a janela abrá, antes não estava respondendo.
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                pass
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()  # Close Window
                quit()  # end pygame
            else:
                pass


