from views.screen import Screen
from controllers.controller import Controller


def main():
    view = Screen()
    game = Controller(view)
    game.run()


if __name__ == "__main__":
    main()