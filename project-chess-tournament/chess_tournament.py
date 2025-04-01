from controllers.menu_controller import MenuController
from models.application import Application
from models.application_menu import ApplicationMenu
from views.menu_view import MenuView

if __name__ == "__main__":
    application_menu = ApplicationMenu()
    application = Application(application_menu)
    menu_view = MenuView()
    menu_controller = MenuController(application, menu_view)
    menu_controller.show_menu()

# 1 commentaire par fonction
# 119
# corriger le bug fin de tour