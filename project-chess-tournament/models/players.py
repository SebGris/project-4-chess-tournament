from typing import Optional
import random
from models.player import Player


class Players(list):

    def get_player(self) -> Optional[Player]:
        """Pop."""
        try:
            return self.pop()
        except IndexError:
            return None

    def get_data(self):
        return [player.get_data() for player in self]

    def shuffle(self):
        """Shuffle players."""
        random.shuffle(self)