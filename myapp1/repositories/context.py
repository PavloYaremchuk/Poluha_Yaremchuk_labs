from .stadium_repository import StadiumRepository
from .team_repository import TeamRepository
from .player_repository import PlayerRepository
from .coach_repository import CoachRepository
from .medical_staff_repository import MedicalStaffRepository
from .player_contract_repository import PlayerContractRepository
from .tournament_repository import TournamentRepository
from .team_in_tournament_repository import TeamInTournamentRepository
from .basketball_match_repository import BasketballMatchRepository
from .player_stats_in_match_repository import PlayerStatsInMatchRepository

class Context:
    def __init__(self):
        self.stadium_repository = StadiumRepository()
        self.team_repository = TeamRepository()
        self.player_repository = PlayerRepository()
        self.coach_repository = CoachRepository()
        self.medical_staff_repository = MedicalStaffRepository()
        self.player_contract_repository = PlayerContractRepository()
        self.tournament_repository = TournamentRepository()
        self.team_in_tournament_repository = TeamInTournamentRepository()
        self.basketball_match_repository = BasketballMatchRepository()
        self.player_stats_in_match_repository = PlayerStatsInMatchRepository()
