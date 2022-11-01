import pygame

#Screen = 200*200 scaled up to X*Y
class GraphicsCard:
    def __init__(self):
        self.width = 32
        self.height = 32
        self.VRAM = [0] * self.width * self.height

        self.screen = pygame.display.set_mode((600, 600))
        self.display = pygame.Surface((self.width, self.height))
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Virtual Graphics Card")
    
    def __clear(self):
        self.display.fill((0, 0, 0))

    def __update(self):
        self.screen.blit(pygame.transform.scale(self.display, (600, 600)), (0, 0))
        pygame.display.update()

    def __tick_virtual_clock(self):
        self.clock.tick(60)

    def __set_at(self, x, y, index):
        self.display.set_at((x, y), (self.VRAM[index] * 17, self.VRAM[index] * 17, self.VRAM[index] * 17))

    def __render_vram(self):
        i = 0
        for y in range(self.width):
            for x in range(self.width):
                self.__set_at(x, y, i)
                i += 1

    def __get_and_handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def tick(self):
        self.__clear()
        self.__render_vram()
        self.__update()
        self.__tick_virtual_clock()