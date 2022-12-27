import pygame


class Letter:
    def __init__(self, font: pygame.font.Font, configs: tuple, letter: str) -> None:
        self.letter = letter
        self.image = font.render(letter, *configs)
        self.rect = self.image.get_rect()


class Line:
    def __init__(
        self, index: int, font: pygame.font.Font, configs: tuple, text: str
    ) -> None:
        self.letters = []
        y = index * font.get_linesize()
        for index, letter in enumerate(text):
            self.letters.append(Letter(font, configs, letter))
            if index == 0:
                x = 0
            else:
                x = self.letters[-2].rect.right
            self.letters[-1].rect.topleft = (x, y)
        size = [0, font.get_linesize()]
        if len(self.letters) > 0:
            size[0] = self.letters[-1].rect.right
        self.rect = pygame.Rect((0, y), size)

    def draw_on(self, surface: pygame.Surface, offset=(0, 0)):
        for letter in self.letters:
            surface.blit(
                letter.image, (letter.rect.x + offset[0], letter.rect.y + offset[1])
            )

    def draw_surface(self):
        if len(self.letters) > 0:
            surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)
            for letter in self.letters:
                surface.blit(letter.image, (letter.rect.x, 0))
            return surface
        else:
            return None


class Text(pygame.sprite.DirtySprite):
    def __init__(
        self,
        font: pygame.font.Font,
        font_color=(0, 0, 0),
        background=None,
        alias=True,
        text="",
    ) -> None:
        super().__init__()
        self.font = font
        self.text = text
        self.lines = []
        self.font_color = font_color
        self.background = background
        self.alias = alias
        self.__set_text(text)

    def __set_text(self, text: str) -> None:
        self.image = None
        self.lines = []
        for index, line_text in enumerate(text.split("\n")):
            self.lines.append(
                Line(
                    index,
                    self.font,
                    (self.alias, self.font_color, self.background),
                    line_text,
                )
            )

    def draw_on(self, surface: pygame.Surface, offset=(0, 0)):
        surface_rect = surface.get_rect()
        for line in self.lines:
            rect = line.rect.copy()
            rect.x += offset[0]
            rect.y += offset[1]
            if rect.colliderect(surface_rect):
                line.draw_on(surface, offset)

    def draw_surface(self):
        w, h = 0, 0
        surfaces = []
        for line in self.lines:
            if (surface := line.draw_surface()) is not None:
                surfaces.append((surface, line.rect))
            w = max(w, line.rect.right)
            h = max(h, line.rect.bottom)
        text_surface = pygame.Surface((w, h), pygame.SRCALPHA)
        for surface, rect in surfaces:
            text_surface.blit(surface, rect)
        return text_surface
