from django.db import models


# Create your models here.
class Department(models.Model):
    title = models.CharField(max_length=32)
    path = models.CharField(max_length=300, null=True, blank=True)


class UserInfo(models.Model):
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
    account = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    creat_time = models.DateTimeField()
    depart = models.ForeignKey(to="Department", to_field="id", on_delete=models.CASCADE)
    gender_choices = {
        (1, "male"),
        (2, "female"),
    }
    gender = models.SmallIntegerField(choices=gender_choices)
