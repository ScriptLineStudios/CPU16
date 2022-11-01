import pygame

#Screen = 200*200 scaled up to X*Y
class GraphicsCard:
    def __init__(self):
        self.width = 20
        self.height = 20
        self.VRAM = [0] * self.width * self.height

        self.screen = pygame.display.set_mode((600, 600))
        self.display = pygame.Surface((20, 20))
        self.clock = pygame.time.Clock()
        
    def tick(self):
        self.display.fill((0, 0, 0))

        i = 0
        for x in range(self.width):
            for y in range(self.width):
                self.display.set_at((x, y), (self.VRAM[i], self.VRAM[i], self.VRAM[i]))
                i += 1

        self.screen.blit(pygame.transform.scale(self.display, (600, 600)), (0, 0))
        pygame.display.update()
        self.clock.tick(60)