from controllers.menu_controller import MenuController
from models.menu_model import MenuModel
from views.menu_view import MenuView


def main():
    menu_model = MenuModel()
    menu_view = MenuView()
    menu_controller = MenuController(menu_model, menu_view)
    menu_controller.start_menu_navigation()


if __name__ == "__main__":
    main()
