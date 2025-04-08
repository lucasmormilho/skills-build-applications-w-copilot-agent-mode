from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create_user(username='john_doe', email='john@example.com', password='password123')
        user2 = User.objects.create_user(username='jane_doe', email='jane@example.com', password='password123')
        
        # Create test teams
        team1 = Team.objects.create(name='Team Alpha', description='Alpha team description')
        team2 = Team.objects.create(name='Team Beta', description='Beta team description')
        
        # Assign users to teams
        team1.members.add(user1)
        team2.members.add(user2)
        
        # Create test activities
        activity1 = Activity.objects.create(name='Running', description='Running activity')
        activity2 = Activity.objects.create(name='Cycling', description='Cycling activity')
        
        # Create test workouts
        Workout.objects.create(user=user1, activity=activity1, duration=30, calories_burned=300)
        Workout.objects.create(user=user2, activity=activity2, duration=45, calories_burned=450)
        
        # Create test leaderboard entries
        Leaderboard.objects.create(user=user1, points=100)
        Leaderboard.objects.create(user=user2, points=150)
        
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
