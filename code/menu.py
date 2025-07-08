#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
import self
from pygame import Surface, Rect
from pygame.examples.moveit import WIDTH
from pygame.font import Font
from code.const import WIN_WIDTH, COLOR_PURPLE, MENU_OPTION, COLOR_WHITE, COLOR_PURPLE2


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menu/menu01.png')  # 0__ Adicionando a imagem no menu
        self.rect = self.surf.get_rect(left=0,
                                       top=0)  # 0__ Adicionando o retangulo para a imagem e identificando onde váo comecar

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu/Menu.mp3')  # 0__ Importando o mp3 do menu
        pygame.mixer_music.play(-1)  # 0__Play para musicar trocar, e o -1 para musica retocar

        while True:  # 0__ Rodando em loop infinito a imagem
            self.window.blit(source=self.surf, dest=self.rect)  # 0__ Aqui esta colocando a img para rodar no retangulo
            self.menu_text(70, "Mountain", COLOR_PURPLE, ((WIN_WIDTH / 2), 100))
            self.menu_text(70, "Shooter", COLOR_PURPLE, ((WIN_WIDTH / 2), 150))

            for i in range(len(MENU_OPTION)):  # 0__ Criando a parte do menu
                if i == menu_option:  # 0___ Se estiver com a opcao ela ficara amarela, mas se nao ela continuara branca if e else
                    self.menu_text(40, MENU_OPTION[i], COLOR_PURPLE2, ((WIN_WIDTH / 2), 360 + 35 * i))

                else:
                    self.menu_text(40, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 360 + 35 * i))

            # Check for all events para conseguir fechar
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:    #Fazendo que desca com a seta para baixo no menu.
                    if event.key == pygame.K_DOWN: #down key
                        if menu_option < len(MENU_OPTION) - 1:   #0__ Fazendo com que pare a seta do menu quando acabar as opcoes
                            menu_option += 1   #0___ Somando para tecla descer
                        else:
                            menu_option = 0  #0___ Fazendo o reset para voltar para o 0
                    if event.key == pygame.K_UP:# UP KEY
                            if menu_option > 0:  # 0__ Fazendo com que pare a seta do menu quando acabar as opcoes
                                menu_option -= 1  # 0___ Somando para tecla descer
                            else:
                                menu_option = len(MENU_OPTION) - 1  # 0___ Fazendo o reset para voltar para o 0
                    if event.key == pygame.K_RETURN:    #0___ ENTER
                        return MENU_OPTION[menu_option]
            pygame.display.flip()

    # 0__ Praticamente o mesmo processo de imagem so que para texto
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
