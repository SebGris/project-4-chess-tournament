from datetime import datetime
import os


class BaseView:
    """Base class for the view, offering generic display methods."""

    @staticmethod
    def clear_console():
        """To clear the console screen."""
        os.system("cls")

    @staticmethod
    def input(prompt: str):
        """Requests a user input with a specific message."""
        return input(prompt.rstrip() + " ").strip()

    @staticmethod
    def input_date(prompt):
        """
        Requests and validates a date in DD/MM/YYYY format.
        Returns a date formatted as text.
        """
        while True:
            date_input = BaseView.input(prompt)
            try:
                date_object = datetime.strptime(date_input, "%d/%m/%Y")
                return date_object.strftime("%d/%m/%Y")
            except ValueError:
                print(
                    "Format invalide. "
                    "Veuillez entrer une date au format JJ/MM/AAAA."
                )
