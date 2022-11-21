from pprint import pp
import pygame
from ..display import Display


class Letter:
    def __init__(self, surface):
        self.surface = surface
        self.size = self.surface.get_size()
        self.pos = []

    def __repr__(self) -> str:
        return repr((self.surface, self.pos))


class Text(pygame.sprite.DirtySprite):
    def __init__(self, text, pos=0):
        super().__init__()
        self.__font = pygame.font.SysFont("arial", 20)
        self.pos = pygame.Vector2(pos)
        self.image = Display.display_surface.copy()
        self.image.fill((0, 0, 0, 0))
        self.rect = self.image.get_rect()

        self.set_text(text)

    def set_text(self, text):
        self.letters = {}
        for line_index, line in enumerate(text.split("\n")):
            self.set_line(line, line_index)
        self.update_image()

    def set_line(self, text, line_index):
        last_right = 0
        line = list(text)
        y = line_index * self.__font.get_linesize()
        for index, letter in enumerate(line):
            if letter not in self.letters.keys():
                self.letters[letter] = Letter(
                    surface=self.__font.render(letter, True, (255, 255, 255))
                )
            rect = self.letters[letter].surface.get_rect()
            rect.y = y
            if index > 0:
                rect.left = last_right
            self.letters[letter].pos.append(rect.topleft)
            last_right = rect.right

    def update_image(self):
        for data in self.letters.values():
            for pos in data.pos:
                self.image.blit(
                    data.surface, (pos[0] + self.pos.x, pos[1] + self.pos.y)
                )
