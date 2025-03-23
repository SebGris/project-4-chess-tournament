from typing import Type, TypeVar
from services.file_service import FileService

T = TypeVar("T")  # Generic type for models


class BaseRepository:
    FOLDER = "data/tournaments"
    FILE_PATH = ""

    def __init__(self, model_class: Type[T]):
        """
        Initializes the repository with a model class
        """
        self.model_class = model_class
        self.file_service = FileService(self.FOLDER, self.FILE_PATH)

    # def get_all(self) -> list[T]:
    #     with open(self.get_file_path(), "r") as file:
    #         return [self.model_class.from_dict(obj) for obj in json.load(file)]

    def get_all(self) -> list[T]:
        return [self.model_class.from_dict(obj) for obj in self.file_service.read_from_file()]

    # def write_all(self, objects: list[T]):
    #     with open(self.get_file_path(), "w") as file:
    #         json.dump([obj.to_dict() for obj in objects], file)

    def write_all(self, objects: list[T]):
        self.file_service.write_to_file([obj.to_dict() for obj in objects])

    def get_by_id(self, id: str) -> T:
        return next((obj for obj in self.get_all() if obj.id == id), None)

    def get_by_ids(self, ids: list[str]) -> list[T]:
        return [obj for obj in self.get_all() if obj.id in ids]

    def save(self, updated_object: T):
        objects = [
            obj for obj in self.get_all() if obj.id != updated_object.id
        ]
        objects.append(updated_object)
        self.write_all(objects)

    def save_all(self, updated_objects: list[T]):
        ids_to_update = {obj.id for obj in updated_objects}
        objects = [
            obj for obj in self.get_all() if obj.id not in ids_to_update
        ]
        objects.extend(updated_objects)
        self.write_all(objects)
