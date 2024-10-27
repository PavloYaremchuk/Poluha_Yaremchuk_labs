from myapp1.models import Stadium
from myapp1.repositories.base_repository import BaseRepository

class StadiumRepository(BaseRepository):
    model = Stadium
