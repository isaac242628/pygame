
import pygame

#conf do pygame
pygame.init()
    
    #define as dimenções da tela
screen = pygame.display.set_mode((1280, 720))
    
    #configura os fps
clock = pygame.time.Clock()

#Variavel que controla o loop
running = True

while running:

    #loop
    for event in pygame.event.get():

        #se
        if event.type == pygame.QUIT:
            
            #define o final do loop
            running = False

    #define a cor da tela
    screen.fill("purple")

    #atualiza a tela
    pygame.display.flip()

    #define a quantidade de fps
    clock.tick(60) 
#finaliza o app
pygame.quit()