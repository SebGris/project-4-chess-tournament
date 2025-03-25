from collections.abc import Iterable
from typing import Type, TypeVar
from services.file_service import FileService

T = TypeVar("T")  # Generic type for models


class BaseRepository:
    FILE_PATH = ""

    def __init__(self, model_class: Type[T]):
        """
        Initializes the repository with a model class
        """
        self.model_class = model_class
        self.file_service = FileService(self.FILE_PATH)

    def _write_all(self, objects: list[T]):
        self.file_service.write_to_file([obj.to_dict() for obj in objects])

    def get_all(self) -> list[T]:
        return [
            self.model_class.from_dict(obj)
            for obj in self.file_service.read_from_file()
        ]

    def get_by_id(self, id: str) -> T:
        return next((obj for obj in self.get_all() if obj.id == id), None)

    def get_by_ids(self, ids: list[str]) -> list[T]:
        return [obj for obj in self.get_all() if obj.id in ids]

    def save(self, updated_objects: list[T]):
        """
        Saves or updates the provided objects in the repository.

        If an object with the same ID already exists, it is replaced.
        Otherwise, the object is added to the repository.

        Args:
            updated_objects (list[T]): A list of objects to save or update.
        """
        # Ensure the input is iterable; if not, wrap it in a list.
        if not isinstance(updated_objects, Iterable):
            updated_objects = [updated_objects]

        # Extract the IDs of the objects to be updated.
        ids_to_update = {obj.id for obj in updated_objects}

        # Filter out existing objects with matching IDs.
        objects = [
            obj for obj in self.get_all() if obj.id not in ids_to_update
        ]

        # Add the updated objects to the list.
        objects.extend(updated_objects)

        # Write the updated list back to the file.
        self._write_all(objects)
