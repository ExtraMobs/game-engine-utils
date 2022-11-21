import pygame

from gameengine import Display, GameEngine, GameResources, Window, widgets


class MainScene(pygame.sprite.LayeredDirty):  # Group subclass
    def __init__(self):
        super().__init__()

        text = widgets.Text("Teste sobre Widgets\nEsse é o widget de texto", (200, 100))

        self.add(text)

        print("Cena principal pronta")

    def update(self):
        super().update()

        if GameEngine.request_quit:
            GameEngine.quit()


if __name__ == "__main__":
    Window.set_title("Text Test")

    Window.set_size((720, 405))
    Display.update_display_from_window()

    GameEngine.set_scene(MainScene())

    GameEngine.start_loop()
