from myapp1.models import MedicalStaff
from myapp1.repositories.base_repository import BaseRepository

class MedicalStaffRepository(BaseRepository):
    model = MedicalStaff