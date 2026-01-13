from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Create users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Tony Stark', team=marvel.name),
            User.objects.create(email='captain@marvel.com', name='Steve Rogers', team=marvel.name),
            User.objects.create(email='batman@dc.com', name='Bruce Wayne', team=dc.name),
            User.objects.create(email='wonderwoman@dc.com', name='Diana Prince', team=dc.name),
        ]

        # Create workouts
        workout1 = Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        workout2 = Workout.objects.create(name='Running', description='Run 5km', difficulty='medium')

        # Create activities
        Activity.objects.create(user=users[0], type='pushups', duration=10, date=timezone.now())
        Activity.objects.create(user=users[1], type='running', duration=30, date=timezone.now())
        Activity.objects.create(user=users[2], type='pushups', duration=15, date=timezone.now())
        Activity.objects.create(user=users[3], type='running', duration=25, date=timezone.now())

        # Create leaderboard
        Leaderboard.objects.create(user=users[0], score=100)
        Leaderboard.objects.create(user=users[1], score=90)
        Leaderboard.objects.create(user=users[2], score=95)
        Leaderboard.objects.create(user=users[3], score=85)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
