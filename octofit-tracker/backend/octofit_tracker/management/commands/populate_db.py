from django.core.management.base import BaseCommand
from mongoengine import connect
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

# Connect to MongoDB
connect('octofit_db', host='localhost', port=27017)

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Check for existing users before creating
        if not User.objects(email='john.doe@example.com'):
            user1 = User(email='john.doe@example.com', name='John Doe', password='password123').save()
        else:
            user1 = User.objects.get(email='john.doe@example.com')

        if not User.objects(email='jane.smith@example.com'):
            user2 = User(email='jane.smith@example.com', name='Jane Smith', password='password123').save()
        else:
            user2 = User.objects.get(email='jane.smith@example.com')

        # Create test teams
        team1 = Team(name='Team Alpha', members=[str(user1.id), str(user2.id)]).save()

        # Create test activities
        Activity(user=user1, activity_type='Running', duration=30, date='2025-04-12').save()
        Activity(user=user2, activity_type='Cycling', duration=45, date='2025-04-12').save()

        # Create test leaderboard entries
        Leaderboard(user=user1, score=100).save()
        Leaderboard(user=user2, score=150).save()

        # Create test workouts
        Workout(name='Push-ups', description='Do 20 push-ups').save()
        Workout(name='Sit-ups', description='Do 30 sit-ups').save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
