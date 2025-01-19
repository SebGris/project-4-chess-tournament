from typing import Optional
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