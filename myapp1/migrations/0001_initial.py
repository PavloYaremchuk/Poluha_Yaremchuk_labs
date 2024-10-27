# Generated by Django 5.1.2 on 2024-10-22 21:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BasketballMatch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("match_time", models.DateTimeField()),
                ("box_score", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("player_name", models.CharField(max_length=50)),
                ("player_surname", models.CharField(max_length=50)),
                ("date_of_birth", models.DateField(blank=True, null=True)),
                (
                    "player_position",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "height",
                    models.DecimalField(
                        blank=True, decimal_places=1, max_digits=4, null=True
                    ),
                ),
                (
                    "weight",
                    models.DecimalField(
                        blank=True, decimal_places=1, max_digits=4, null=True
                    ),
                ),
                ("player_number", models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Stadium",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stadium_name", models.CharField(max_length=50)),
                ("city", models.CharField(blank=True, max_length=50, null=True)),
                ("capacity", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="PlayerContract",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("contract_start", models.DateField()),
                ("contract_end", models.DateField()),
                ("price", models.IntegerField()),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contracts",
                        to="myapp1.player",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PlayerStatsInMatch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("gametime", models.DecimalField(decimal_places=2, max_digits=4)),
                ("points", models.IntegerField(blank=True, null=True)),
                ("rebounds", models.IntegerField(blank=True, null=True)),
                ("assists", models.IntegerField(blank=True, null=True)),
                ("steals", models.IntegerField(blank=True, null=True)),
                ("blocks", models.IntegerField(blank=True, null=True)),
                (
                    "match",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="player_stats",
                        to="myapp1.basketballmatch",
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="match_stats",
                        to="myapp1.player",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="basketballmatch",
            name="stadium",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="matches",
                to="myapp1.stadium",
            ),
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("team_name", models.CharField(max_length=50)),
                ("year_of_start", models.IntegerField(blank=True, null=True)),
                (
                    "stadium",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="teams",
                        to="myapp1.stadium",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="player",
            name="team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="players",
                to="myapp1.team",
            ),
        ),
        migrations.CreateModel(
            name="MedicalStaff",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("medical_staff_name", models.CharField(max_length=50)),
                ("medical_staff_surname", models.CharField(max_length=50)),
                ("date_of_birth", models.DateField(blank=True, null=True)),
                ("specialization", models.IntegerField(blank=True, null=True)),
                ("experience", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="medical_staff",
                        to="myapp1.team",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Coach",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("coach_name", models.CharField(max_length=50)),
                ("coach_surname", models.CharField(max_length=50)),
                ("date_of_birth", models.DateField(blank=True, null=True)),
                ("specialization", models.IntegerField(blank=True, null=True)),
                ("experience", models.CharField(blank=True, max_length=50, null=True)),
                ("salary", models.IntegerField()),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="coaches",
                        to="myapp1.team",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="basketballmatch",
            name="team1",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="matches_as_team1",
                to="myapp1.team",
            ),
        ),
        migrations.AddField(
            model_name="basketballmatch",
            name="team2",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="matches_as_team2",
                to="myapp1.team",
            ),
        ),
        migrations.CreateModel(
            name="Tournament",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tournament_name", models.CharField(max_length=50)),
                ("tournament_start", models.DateField()),
                ("tournament_end", models.DateField()),
                ("tournament_type", models.IntegerField(blank=True, null=True)),
                ("grid", models.TextField(blank=True, null=True)),
                (
                    "winner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="won_tournaments",
                        to="myapp1.team",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TeamInTournament",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tournaments",
                        to="myapp1.team",
                    ),
                ),
                (
                    "tournament",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="teams",
                        to="myapp1.tournament",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="basketballmatch",
            name="tournament",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="matches",
                to="myapp1.tournament",
            ),
        ),
    ]
