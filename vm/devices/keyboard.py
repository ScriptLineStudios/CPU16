import pygame

class Keyboard:
    def __init__(self, screen):
        self.screen = screen
        
        self.KEYDATA = [0] * 1000
    
    def tick(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.KEYDATA[ord(event.unicode)] = 1
            if event.type == pygame.KEYUP:
                self.KEYDATA[ord(event.unicode)] = 0
