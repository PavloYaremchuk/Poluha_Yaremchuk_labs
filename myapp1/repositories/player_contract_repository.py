from myapp1.models import PlayerContract
from myapp1.repositories.base_repository import BaseRepository

class PlayerContractRepository(BaseRepository):
    model = PlayerContract