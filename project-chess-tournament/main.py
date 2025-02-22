from controllers.controller import Controller
from models.menu import Menu
from views.view import View


if __name__ == "__main__":
    menu = Menu()
    view = View()
    controller = Controller(menu, view)
    controller.run()
