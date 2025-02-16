from controllers.menu_controller import MenuController
from models.menu_model import MenuModel
from views.menu_view import MenuView


def main():
    model = MenuModel()
    view = MenuView()
    controller = MenuController(model, view)
    controller.show_menu()


if __name__ == "__main__":
    main()
