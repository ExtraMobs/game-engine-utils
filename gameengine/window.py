import pygame
import pygame._sdl2


class Window:
    _sdl2_window = None
    surface = None
    size = (1, 1)

    @classmethod
    def get_size(cls):
        return cls._sdl2_window.size

    @classmethod
    def set_size(cls, size, *flags):
        flag = 0
        for f in flags:
            flag |= f
        cls.surface = pygame.display.set_mode(size, flag)
        Window._sdl2_window = pygame._sdl2.Window.from_display_module()

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
