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

    def getParList(self):
        # create a list of the pars for each hole in the course
        holes = Hole.objects.filter(hole_course_id = self.course_id)
        hole_par_values = []
        for each in holes:
            hole_par_values.append(each.hole_par)
        return hole_par_values

class Hole(models.Model):
    hole_id = models.AutoField(primary_key=True)
    hole_course = models.ForeignKey(GolfCourse, models.DO_NOTHING)
    hole_number = models.IntegerField()
    hole_par = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Hole'
    
    def __str__(self):
        return "{}, Hole {}, Par {}".format (self.hole_course.course_name,
                                             self.hole_number, self.hole_par)
