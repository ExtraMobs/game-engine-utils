from gameengine import GameEngine, Window

size = (720, 405)

if __name__ == "__main__":
    # Window.set_size((720, 405))
    Window.set_size(size)

    GameEngine.start_loop()
