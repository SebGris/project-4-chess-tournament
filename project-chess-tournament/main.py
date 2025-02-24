from controllers.controller_menu import ControllerMenu
from models.menu import Menu
from views.view import View


if __name__ == "__main__":
    menu = Menu()
    view = View()
    controller = ControllerMenu(menu, view)
    controller.run()
