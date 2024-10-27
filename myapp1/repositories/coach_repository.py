from myapp1.models import Coach
from myapp1.repositories.base_repository import BaseRepository

class CoachRepository(BaseRepository):
    model = Coach