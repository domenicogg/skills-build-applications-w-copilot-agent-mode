from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout

# Remove admin registration for mongoengine models as they are not compatible with Django admin
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('email', 'name')

# @admin.register(Team)
# class TeamAdmin(admin.ModelAdmin):
#     list_display = ('name',)

# @admin.register(Activity)
# class ActivityAdmin(admin.ModelAdmin):
#     list_display = ('user', 'activity_type', 'duration', 'date')

# @admin.register(Leaderboard)
# class LeaderboardAdmin(admin.ModelAdmin):
#     list_display = ('user', 'score')

# @admin.register(Workout)
# class WorkoutAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description')