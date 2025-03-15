import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))

#class
class Rect():
    #properties
    def __init__(self,color,dimensions):
        self.surface = screen
        self.color = color
        self.dimensions = dimensions
    #fonctions
    def draw (self):
        self.rect = pygame .draw.rect(self.surface,self.color,self.dimensions)

#objects
rect_blue = Rect("blue",(50,50,100,100))
rect_red = Rect("red",(200,200,250,250))
#mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    rect_blue.draw()
    rect_red.draw()
    pygame.display.update()
pygame.quit()






