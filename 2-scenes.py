import pygame

from gameengine import Display, Engine, Scene, Window, objects


class RectSprite(objects.GraphicObject):  # Sprite subclass
    def __init__(self):
        super().__init__()

        self.surface = pygame.Surface((100, 100))
        self.surface.fill("RED")

        # centering the rectangle
        surface_size = self.surface.get_size()
        self.position.xy = Display.surface.get_rect().center
        self.position.x -= surface_size[0] / 2
        self.position.y -= surface_size[1] / 2


class MainScene(Scene):  # Group subclass
    def __init__(self):
        super().__init__()

        self.add_child(RectSprite())

        print("Cena principal pronta")

    def process(self):
        super().process()

        if Engine.request_quit:
            Engine.system_exit()


if __name__ == "__main__":
    Window.set_title("Scenes Test")

    Window.set_size((720, 405))
    Display.update_display_from_window()

    Engine.set_scene(MainScene())

    Engine.start_loop()
