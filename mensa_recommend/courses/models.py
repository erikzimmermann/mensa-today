from django.db import models


class Course(models.Model):
    publishId = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    learnweb_abbr = models.CharField(max_length=50)
    users = models.ManyToManyField("users.User")


class Timeslot(models.Model):
    weekDay = models.CharField(max_length=50)
    startTime = models.TimeField()
    endTime = models.TimeField()
    startDate = models.DateField(auto_now=False, auto_now_add=False, null=True)
    endDate = models.DateField(auto_now=False, auto_now_add=False, null=True)
    rythm = models.CharField(max_length=10)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['weekDay', 'startTime', 'endTime', 'rythm', 'startDate', 'endDate'], name='unique timeslot')
        ]


class Room(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=80)
    seats = models.IntegerField(null=True)


class Reservation(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    timeslot = models.ForeignKey(Timeslot, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
