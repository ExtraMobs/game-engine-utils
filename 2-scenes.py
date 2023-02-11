import pygame

from gameengine import Display, Engine, Window


class RectSprite(pygame.sprite.DirtySprite):  # Sprite subclass
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((100, 100))
        self.image.fill("RED")

        self.rect = self.image.get_rect()

        self.rect.center = Display.surface.get_rect().center


class MainScene(pygame.sprite.LayeredDirty):  # Group subclass
    def __init__(self):
        super().__init__()

        self.add(RectSprite())

        print("Cena principal pronta")

    def update(self):
        super().update()

        if Engine.request_quit:
            Engine.system_exit()


if __name__ == "__main__":
    Window.set_title("Scenes Test")

    Window.set_size((720, 405))
    Display.update_display_from_window()

    Engine.set_scene(MainScene())

    Engine.start_loop()
