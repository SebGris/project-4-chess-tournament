from datetime import datetime
import os


class View:
    """Base class for the view, offering generic display methods."""

    @staticmethod
    def clear_console():
        """To clear the console screen."""
        os.system("cls")

    @staticmethod
    def display_message(message):
        """Displays a generic message."""
        print(message)

    @staticmethod
    def get_input(prompt):
        """Requests a user input with a specific message."""
        prompt = prompt.rstrip() + " "
        return input(prompt).strip()

    @staticmethod
    def get_input_date(prompt):
        """
        Requests and validates a date in DD/MM/YYYY format.
        Returns a date formatted as text.
        """
        while True:
            date_input = View.get_input(prompt)
            try:
                date_object = datetime.strptime(date_input, "%d/%m/%Y")
                return date_object.strftime("%d/%m/%Y")
            except ValueError:
                print(
                    "Format invalide. "
                    "Veuillez entrer une date au format JJ/MM/AAAA."
                    )
    @staticmethod
    def quit():
        print("Au revoir !")
