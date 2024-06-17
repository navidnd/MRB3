from django.db import models

# Create your models here.

class mainPlanInfo(models.Model):

    plan_name = models.CharField(max_length=150)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    duration = models.PositiveSmallIntegerField()


class eachPlanDayInfo(models.Model):

    movement_name = models.CharField(max_length=150)
    movement_sets = models.PositiveSmallIntegerField()
    movement_reps = models.PositiveSmallIntegerField()
    movement_rest = models.PositiveSmallIntegerField()

