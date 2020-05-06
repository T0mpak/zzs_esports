from django.db import models
from datetime import date


class MostValuablePlayer(models.Model):
    """MVP Игроки"""
    nickname = models.CharField("Ник", max_length=150)
    first_name = models.CharField("Имя", max_length=100, default="NNN")
    last_name = models.CharField("Фамилия", max_length=100, default="NNN")

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = "MVP player"
        verbose_name_plural = "MVP players"


class Match(models.Model):
    """Матчи"""
    teams = models.CharField("Команды", max_length=300, default="ZZS - ")
    score = models.CharField("Счет", max_length=50)
    mvp_player = models.ForeignKey(MostValuablePlayer, verbose_name="MVP игрок", on_delete=models.SET_NULL, null=True)
    win_result = models.BooleanField("Победа", default=True)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.teams

    class Meta:
        verbose_name = "Match"
        verbose_name_plural = "Matches"


class Team(models.Model):
    """Команды"""
    name = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
    team_started = models.DateField("Дата основания", default=date.today)
    matches = models.ManyToManyField(Match, verbose_name="Матчи", related_name="teams_games")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"


class Event(models.Model):
    """Турниры"""
    name = models.CharField("Название", max_length=250)
    description = models.TextField("Описание")
    date = models.DateField("Дата проведения", default=date.today)
    prize_pool = models.IntegerField("Призовой фонд", default=0, help_text="указывать сумму в тенге")
    lan = models.BooleanField("True- LAN, False- Online", default=False)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"


class Stat(models.Model):
    """Статистика"""
    players_stat = models.ForeignKey(
        MostValuablePlayer, verbose_name="Статистика игрока", on_delete=models.SET_NULL, null=True
    )
    kd_ratio = models.FloatField("КД", default=1.00)
    head_shots = models.FloatField("Процент хедшотов", default=0.00)
    maps_played = models.IntegerField("Сыгранно карт", default=0)
    elo = models.PositiveSmallIntegerField("ОЧКОв ЭЛО", default=1000)
    face_it_lvl = models.PositiveSmallIntegerField("Уровень на FACEIT", default=3)

    def __str__(self):
        return f"{self.kd_ratio}"

    class Meta:
        verbose_name = "Stat"
        verbose_name_plural = "Stats"


class Player(models.Model):
    """Игроки"""
    player = models.ForeignKey(MostValuablePlayer, verbose_name="игрок", on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField("Возраст", default=16)
    role = models.CharField("Роль", max_length=150)
    photo = models.ImageField("Фото", upload_to="player/")
    active_period = models.CharField("Период активности", max_length=150)
    country = models.CharField("Страна", max_length=100)
    team = models.ManyToManyField(Team, verbose_name="команда", related_name="team_player")
    stat = models.ForeignKey(Stat, verbose_name="статистика", on_delete=models.CASCADE)
    event = models.ManyToManyField(Event, verbose_name="турниры", related_name="event_player")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return f"{self.player}"

    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players"


class Highlight(models.Model):
    """Хайлайты"""
    player = models.ForeignKey(Player, verbose_name="игрок", on_delete=models.SET_NULL, null=True)
    match = models.ForeignKey(Match, verbose_name="матч", on_delete=models.SET_NULL, null=True)
    description = models.TextField("Название")
    preview = models.ImageField("Превью", upload_to="preview/")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Highlight"
        verbose_name_plural = "Highlights"


class Comments(models.Model):
    """Коментарии"""
    name = models.CharField("Имя", max_length=150)
    email = models.EmailField()
    text = models.TextField("Текст")
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    highlight = models.ForeignKey(Highlight, verbose_name="хайлайт", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.highlight}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"