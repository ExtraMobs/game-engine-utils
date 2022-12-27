import pygame


class Window:
    surface = None
    size = (1, 1)

    @classmethod
    def get_size(cls):
        return cls.surface.get_size()

    @classmethod
    def set_size(cls, size, *flags):
        flag = 0
        for f in flags:
            flag |= f
        cls.surface = pygame.display.set_mode(size, flag)

    @classmethod
    def get_rect(self):
        return self.surface.get_rect()

    @classmethod
    def set_title(cls, title):
        pygame.display.set_caption(title)

    @classmethod
    def get_title(cls):
        return cls._sdl2_window.title

    @classmethod
    def get_window_sdl2(cls):
        return cls._sdl2_window
