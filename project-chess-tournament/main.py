from controllers.controller_menu import ControllerMenu
from models.menu import Menu
from views.menu_view import MenuView


if __name__ == "__main__":
    menu = Menu()
    menu_view = MenuView()
    controller = ControllerMenu(menu, menu_view)
    controller.run()
