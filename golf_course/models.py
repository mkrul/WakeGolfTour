from django.db import models


class GolfCourse(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course_name = models.TextField()
    course_total_par = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'GolfCourse'
        verbose_name = 'Golf Course'
        verbose_name_plural = 'Golf Courses'

    def __str__(self):
        return self.course_name


class Hole(models.Model):
    hole_id = models.IntegerField(primary_key=True)
    hole_course = models.ForeignKey(GolfCourse, models.DO_NOTHING)
    hole_number = models.IntegerField()
    hole_par = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Hole'
    
    def __str__(self):
        return "{}, Hole {}, Par {}".format (self.hole_course.course_name,
                                             self.hole_number, self.hole_par)
