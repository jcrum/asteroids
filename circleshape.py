import pygame
import math

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass


    def __distance(self, shape):
        x1, y1 = self.position
        x2, y2 = shape.position

        return abs(math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2)))

    def collision(self, shape):
        distance = self.__distance(shape)

        if distance < (self.radius + shape.radius):
            return True
        
        return False
