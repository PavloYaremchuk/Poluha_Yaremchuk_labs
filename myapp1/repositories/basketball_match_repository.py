from myapp1.models import BasketballMatch
from myapp1.repositories.base_repository import BaseRepository

class BasketballMatchRepository(BaseRepository):
    model = BasketballMatch