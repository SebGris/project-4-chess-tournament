from controllers.menu_controller import MenuController
from models.application import Application
from views.menu_view import MenuView

if __name__ == "__main__":
    application = Application()
    menu_view = MenuView()
    menu_controller = MenuController(application, menu_view)
    menu_controller.show_menu()
