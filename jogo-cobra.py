import pygame
# Inicializando módulos de Pygame
pygame.init()
# Criando uma janela com o título “Olá, mundo!”
janela = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Olá, mundo!')

deve_continuar = True

while deve_continuar:
for event in pygame.event.get():

if event.type == pygame.QUIT:
  deve_continuar = False


pygame.quit() 
