from gameengine import GameEngine, Window

size = (720, 405)

if __name__ == "__main__":
    # Window.set_size((720, 405))

    Window.set_size(size)
    # Display.update_display_from_window()

    GameEngine.start_loop()
