from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='Marvel', is_superhero=True),
            User(email='captain@marvel.com', name='Captain America', team='Marvel', is_superhero=True),
            User(email='batman@dc.com', name='Batman', team='DC', is_superhero=True),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='DC', is_superhero=True),
        ]
        User.objects.bulk_create(users)

        # Activities
        activities = [
            Activity(user='Iron Man', activity_type='Running', duration=30),
            Activity(user='Captain America', activity_type='Cycling', duration=45),
            Activity(user='Batman', activity_type='Swimming', duration=25),
            Activity(user='Wonder Woman', activity_type='Yoga', duration=40),
        ]
        Activity.objects.bulk_create(activities)

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=65)

        # Workouts
        workouts = [
            Workout(name='Super Strength', difficulty='Hard'),
            Workout(name='Flight Training', difficulty='Medium'),
            Workout(name='Stealth Moves', difficulty='Easy'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
