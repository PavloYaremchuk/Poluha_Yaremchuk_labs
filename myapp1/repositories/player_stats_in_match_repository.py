from myapp1.models import PlayerStatsInMatch
from myapp1.repositories.base_repository import BaseRepository

class PlayerStatsInMatchRepository(BaseRepository):
    model = PlayerStatsInMatch