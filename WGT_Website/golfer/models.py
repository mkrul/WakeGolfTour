from django.db import models
from tournament.models import Tournament, Round
from golf_course.models import GolfCourse

class Golfer(models.Model):
    golfer_id = models.IntegerField(primary_key=True)
    golfer_name = models.TextField()
    golfer_birthdate = models.DateField()

    class Meta:
        managed = False
        db_table = 'Golfer'

    def __str__(self):
        return self.golfer_name


class TournGolfer(models.Model):
    tg_id = models.IntegerField(primary_key=True)
    tg_tourn = models.ForeignKey(Tournament, models.DO_NOTHING)
    tg_golfer = models.ForeignKey(Golfer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'TournGolfer'
        verbose_name = 'Tournament Golfer'
        verbose_name_plural = 'Tournament Golfers'

    def __str__(self):
        return "{} {}".format (self.tg_tourn.tourn_name,
                               self.tg_golfer.golfer_name)


class GolferRoundScores(models.Model):
    grs_id = models.IntegerField(primary_key=True)
    grs_tourn_golfer = models.ForeignKey(TournGolfer, models.DO_NOTHING)
    grs_round = models.ForeignKey(Round, models.DO_NOTHING)
    grs_total_score = models.IntegerField()
    grs_hole1_score = models.IntegerField()
    grs_hole2_score = models.IntegerField()
    grs_hole3_score = models.IntegerField()
    grs_hole4_score = models.IntegerField()
    grs_hole5_score = models.IntegerField()
    grs_hole6_score = models.IntegerField()
    grs_hole7_score = models.IntegerField()
    grs_hole8_score = models.IntegerField()
    grs_hole9_score = models.IntegerField()
    grs_hole10_score = models.IntegerField()
    grs_hole11_score = models.IntegerField()
    grs_hole12_score = models.IntegerField()
    grs_hole13_score = models.IntegerField()
    grs_hole14_score = models.IntegerField()
    grs_hole15_score = models.IntegerField()
    grs_hole16_score = models.IntegerField()
    grs_hole17_score = models.IntegerField()
    grs_hole18_score = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'GolferRoundScores'
        verbose_name = 'Golfer Round Scores'
        verbose_name_plural = 'Golfers Round Scores'

    def __str__(self):
        return "{} {} {} {}".format (self.grs_tourn_golfer.tg_golfer,
                                     self.grs_tourn_golfer.tg_tourn,
                                     self.grs_round, self.grs_total_score)
