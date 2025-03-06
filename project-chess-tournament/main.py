from controllers.menu_controller import MenuController
from models.menu import Menu
from views.menu_view import MenuView


if __name__ == "__main__":
    menu = Menu()
    menu_view = MenuView()
    controller = MenuController(menu, menu_view)
    controller.run()
