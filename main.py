import pygame #Importando o pygame

print("Setup Start") #Para depurar, saber onde o código está abrindo para identificar algum erro
pygame.init() #Ativando o pygame
window = pygame.display.set_mode(size=(600, 480)) #Definir o tamanho da tela
print("Setup end") #Para depurar, saber onde o código está fechando, para identificar algum erro.

print("Loop Start")
while True: #Fazendo com que a janela abrá, antes não estava respondendo.
    #Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Close Window
            quit() #end pygame

