import pygame
pygame.init()
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((600,600))
pygame.display.update()

class Circle():
    def __init__(self,color,pos,radius,width):
        self.circle_color = color
        self.circle_pos = pos
        self.circle_radius = radius
        self.circle_width = width
        self.circle_surface = screen

    def draw(self):
       pygame.draw.circle(self.circle_surface, self.circle_color, self.circle_pos, self.circle_radius, self.circle_width)
    def grow(self,r):
        self.circle_radius = self.circle_radius + r
        pygame.draw.circle(self.circle_surface, self.circle_color, self.circle_pos, self.circle_radius, self.circle_width)

circle = Circle("blue",(300,300),25,0)

#mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            circle.draw()
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            circle.grow(10)
            pygame.display.update()
        if event.type == pygame.MOUSEMOTION:
             pos = pygame.mouse.get_pos()
             circle = Circle("yellow",(22,22),5,5)
             circle.draw()
             pygame.display.update()

