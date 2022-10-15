import pygame
from math import sin, cos, radians
pygame.init()

LBLUE = (100,100,255)
RADIUS = 100
DEPTH = 5

class Circle:
    def __init__(self,position: pygame.Vector2, depth: int = 0) -> None:
        self.pos = position
        self.circles = []
        if depth > 0:
            print(depth)
            self.circles.append(Circle(pygame.Vector2(self.pos.x, self.pos.y + RADIUS), depth-1))
            self.circles.append(Circle(pygame.Vector2(self.pos.x, self.pos.y - RADIUS), depth-1))
            self.circles.append(Circle(pygame.Vector2(self.pos.x + (RADIUS * sin(radians(60))), self.pos.y + (RADIUS * cos(radians(60)))), depth-1))
            self.circles.append(Circle(pygame.Vector2(self.pos.x - (RADIUS * sin(radians(60))), self.pos.y - (RADIUS * cos(radians(60)))), depth-1))
            self.circles.append(Circle(pygame.Vector2(self.pos.x - (RADIUS * sin(radians(60))), self.pos.y + (RADIUS * cos(radians(60)))), depth-1))
            self.circles.append(Circle(pygame.Vector2(self.pos.x + (RADIUS * sin(radians(60))), self.pos.y - (RADIUS * cos(radians(60)))), depth-1))
    
    def draw(self, screen):
        pygame.draw.circle(screen, LBLUE, self.pos, RADIUS, 1)
        for c in self.circles:
            c.draw(screen)


screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Circle Drawing")
running = True
center = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

mainCircle = Circle(center,DEPTH)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LCTRL]:
        running = False
    
    mainCircle.draw(screen)

    pygame.display.flip()
pygame.quit()