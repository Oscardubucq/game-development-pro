import pygame
import time
pygame.init()
WIDTH = 1000
HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("greeting card")

image = pygame.image.load("cake.jpg")
img = pygame.transform.scale(image,(WIDTH,HEIGHT))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    font = pygame.font.SysFont("Arial",72)
    text = font.render("joyeux anniversair",True,(0,0,0))
    screen.blit(img,(0,0))
    screen.blit(text,(200,200))
    pygame.display.update()
    time.sleep(2)

    image2 = pygame.image.load("cadeau.jpg")
    img2 = pygame.transform.scale(image2,(WIDTH,HEIGHT))
    font2 = pygame.font.SysFont("Arial",72)
    text2 = font.render("j'ai un cadeau pour mon ami",True,(0,0,0))
    screen.blit(img2,(0,0))
    screen.blit(text2,(200,200))
    pygame.display.update()
    time.sleep(2)

