from myapp1.models import Tournament
from myapp1.repositories.base_repository import BaseRepository

class TournamentRepository(BaseRepository):
    model = Tournament