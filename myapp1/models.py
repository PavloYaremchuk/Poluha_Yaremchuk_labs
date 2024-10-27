from django.db import models

# Модель Stadium
class Stadium(models.Model):
    stadium_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50, null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.stadium_name}, {self.city}, {self.capacity}'

    class Meta:
        db_table = 'stadium'

# Модель Team
class Team(models.Model):
    team_name = models.CharField(max_length=50)
    year_of_start = models.IntegerField(null=True, blank=True)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, related_name='teams')

    def __str__(self):
        return self.team_name

    class Meta:
        db_table = 'team'


# Модель Player
class Player(models.Model):
    player_name = models.CharField(max_length=50)
    player_surname = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    player_position = models.CharField(max_length=20, null=True, blank=True)
    height = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    weight = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    player_number = models.IntegerField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')

    def __str__(self):
        return f"{self.player_name} {self.player_surname}"

    class Meta:
        db_table = 'player'


# Модель Coach
class Coach(models.Model):
    coach_name = models.CharField(max_length=50)
    coach_surname = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    specialization = models.IntegerField(null=True, blank=True)
    experience = models.CharField(max_length=50, null=True, blank=True)
    salary = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='coaches')

    def __str__(self):
        return f"{self.coach_name} {self.coach_surname}"

    class Meta:
        db_table = 'coach'


# Модель MedicalStaff
class MedicalStaff(models.Model):
    medical_staff_name = models.CharField(max_length=50)
    medical_staff_surname = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    specialization = models.IntegerField(null=True, blank=True)
    experience = models.CharField(max_length=50, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='medical_staff')

    def __str__(self):
        return f"{self.medical_staff_name} {self.medical_staff_surname}"

    class Meta:
        db_table = 'medical_staff'


# Модель PlayerContract
class PlayerContract(models.Model):
    contract_start = models.DateField()
    contract_end = models.DateField()
    price = models.IntegerField()
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='contracts')

    def __str__(self):
        return f"Contract for {self.player}"

    class Meta:
        db_table = 'contract_contract'


# Модель Tournament
class Tournament(models.Model):
    tournament_name = models.CharField(max_length=50)
    tournament_start = models.DateField()
    tournament_end = models.DateField()
    tournament_type = models.IntegerField(null=True, blank=True)
    grid = models.TextField(null=True, blank=True)
    winner = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='won_tournaments')

    def __str__(self):
        return self.tournament_name

    class Meta:
        db_table = 'tournament'


# Модель TeamInTournament
class TeamInTournament(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='tournaments')
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='teams')

    def __str__(self):
        return f"{self.team} in {self.tournament}"

    class Meta:
        db_table = 'team_in_tournament'


# Модель BasketballMatch
class BasketballMatch(models.Model):
    match_time = models.DateTimeField()
    box_score = models.TextField()
    stadium = models.ForeignKey(Stadium, on_delete=models.SET_NULL, null=True, blank=True, related_name='matches')
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches_as_team1')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches_as_team2')
    tournament = models.ForeignKey(Tournament, on_delete=models.SET_NULL, null=True, blank=True, related_name='matches')

    def __str__(self):
        return f"{self.team1} vs {self.team2} at {self.match_time}"

    class Meta:
        db_table = 'basketball_match'


# Модель PlayerStatsInMatch
class PlayerStatsInMatch(models.Model):
    gametime = models.DecimalField(max_digits=4, decimal_places=2)
    points = models.IntegerField(null=True, blank=True)
    rebounds = models.IntegerField(null=True, blank=True)
    assists = models.IntegerField(null=True, blank=True)
    steals = models.IntegerField(null=True, blank=True)
    blocks = models.IntegerField(null=True, blank=True)
    match = models.ForeignKey(BasketballMatch, on_delete=models.CASCADE, related_name='player_stats')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='match_stats')

    def __str__(self):
        return f"{self.player} stats in match {self.match}"

    class Meta:
        db_table = 'player_stats_in_match'
