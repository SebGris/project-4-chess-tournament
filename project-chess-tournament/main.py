from controllers.controller_menu import ControllerMenu
from models.menu import Menu
from views.menu_view import MenuView


if __name__ == "__main__":
    menu = Menu()
    menuview = MenuView()
    controller = ControllerMenu(menu, menuview)
    controller.run()
