from ssl import Options
from django.db import models
from django.core.validators import *
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from datetime import date
from django.utils.translation import gettext_lazy as text  # import gettext_lazy


def validate_stroke(stroke):
    STROKE_CHOICES = ['front crawl', 'butterfly',
                      'breast', 'back', 'freestyle']
    if stroke not in STROKE_CHOICES:
        raise ValidationError(
            text(f"{stroke} is not valid. Please select a valid stroke type."))


class SwimRecord(models.Model):

    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False, default=None)
    team_name = models.CharField(max_length=255, null=False, default=None)
    relay = models.BooleanField(default=True)
    stroke = models.CharField(max_length=255, validators=[
                              validate_stroke], null=False, default=None)
    distance = models.IntegerField(
        validators=[MinValueValidator(50)], null=False, default=None)
    record_date = models.DateTimeField(
        validators=[MaxValueValidator(limit_value=date.today)], default=None)
    record_broken_date = models.DateTimeField(validators=[MaxValueValidator(limit_value=record_date)], default=None)
