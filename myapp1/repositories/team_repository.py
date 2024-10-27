from myapp1.models import Team
from myapp1.repositories.base_repository import BaseRepository

class TeamRepository(BaseRepository):
    model = Team