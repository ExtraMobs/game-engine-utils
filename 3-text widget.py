import pygame

from gameengine import Display, Engine, Window, utils


class Label(pygame.sprite.DirtySprite):
    def __init__(self):
        super().__init__()
        text = utils.Text(
            "Teste sobre Widgets\nEsse é o widget de texto",
            pygame.font.SysFont("arial", 20),
            (255, 255, 255),
        )
        self.image = text.draw_surface()
        self.rect = self.image.get_rect()
        self.rect.topleft = (200, 100)


class MainScene(pygame.sprite.LayeredDirty):  # Group subclass
    def __init__(self):
        super().__init__()

        self.add(Label())

        print("Cena principal pronta")

    def update(self):
        super().update()

        if Engine.request_quit:
            Engine.system_exit()


if __name__ == "__main__":
    Window.set_title("Text Test")

    Window.set_size((720, 405))
    Display.update_display_from_window()

    Engine.set_scene(MainScene())

    Engine.start_loop()
