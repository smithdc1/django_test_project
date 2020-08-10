from django.db import models

# Create your models here.

from django.db import models


class Boolean(models.Model):
    both_false = models.BooleanField(null=False, blank=False)
    both_true = models.BooleanField(null=True, blank=True)
    null_true = models.BooleanField(null=True, blank=False)
    blank_true = models.BooleanField(null=False, blank=True)


class Choices(models.Model):
    choices = (
        (True, 'Yes!'),
        (False, 'No!'),
    )
    both_false = models.BooleanField(null=False, blank=False, choices=choices)
    both_true = models.BooleanField(null=True, blank=True, choices=choices)
    null_true = models.BooleanField(null=True, blank=False, choices=choices)
    blank_true = models.BooleanField(null=False, blank=True, choices=choices)


class Default(models.Model):
    both_false = models.BooleanField(null=False, blank=False, default=True)
    both_true = models.BooleanField(null=True, blank=True, default=True)
    null_true = models.BooleanField(null=True, blank=False, default=True)
    blank_true = models.BooleanField(null=False, blank=True, default=True)


class ChoicesAndDefault(models.Model):
    choices = (
        (True, 'Yes!'),
        (False, 'No!'),
    )
    both_false = models.BooleanField(null=False, blank=False, choices=choices, default=True)
    both_true = models.BooleanField(null=True, blank=True, choices=choices, default=True)
    null_true = models.BooleanField(null=True, blank=False, choices=choices, default=True)
    blank_true = models.BooleanField(null=False, blank=True, choices=choices, default=True)
