from myapp1.models import Player
from myapp1.repositories.base_repository import BaseRepository

class PlayerRepository(BaseRepository):
    model = Player