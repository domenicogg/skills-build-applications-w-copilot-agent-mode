from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Team, Activity, Leaderboard, Workout

class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        data = [{"email": user.email, "name": user.name} for user in users]
        return Response(data)

class TeamListView(APIView):
    def get(self, request):
        teams = Team.objects.all()
        data = [{"name": team.name, "members": team.members} for team in teams]
        return Response(data)

class ActivityListView(APIView):
    def get(self, request):
        activities = Activity.objects.all()
        data = [{"name": activity.name, "duration": activity.duration} for activity in activities]
        return Response(data)

class LeaderboardListView(APIView):
    def get(self, request):
        leaderboards = Leaderboard.objects.all()
        data = [{"user": leaderboard.user, "score": leaderboard.score} for leaderboard in leaderboards]
        return Response(data)

class WorkoutListView(APIView):
    def get(self, request):
        workouts = Workout.objects.all()
        data = [{"name": workout.name, "calories_burned": workout.calories_burned} for workout in workouts]
        return Response(data)