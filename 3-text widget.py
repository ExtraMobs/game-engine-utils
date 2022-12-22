import pygame

from gameengine import Display, Engine, Window, widgets


class MainScene(pygame.sprite.LayeredDirty):  # Group subclass
    def __init__(self):
        super().__init__()

        text = widgets.Text("Teste sobre Widgets\nEsse é o widget de texto", (200, 100))

        self.add(text)

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
