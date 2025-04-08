from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # ...additional fields...

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)
    # ...additional fields...

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    # ...additional fields...

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField()
    # ...additional fields...

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # ...additional fields...
