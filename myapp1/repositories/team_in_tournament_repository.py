from myapp1.models import TeamInTournament
from myapp1.repositories.base_repository import BaseRepository

class TeamInTournamentRepository(BaseRepository):
    model = TeamInTournament