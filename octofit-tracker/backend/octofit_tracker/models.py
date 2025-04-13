from mongoengine import Document, StringField, IntField, ListField, ReferenceField, DateField

class User(Document):
    email = StringField(required=True, unique=True)
    name = StringField(max_length=255, required=True)
    password = StringField(max_length=255, required=True)

class Team(Document):
    name = StringField(max_length=255, required=True)
    members = ListField(StringField())

class Activity(Document):
    user = ReferenceField(User, required=True)
    activity_type = StringField(max_length=255, required=True)
    duration = IntField(required=True)
    date = DateField(required=True)

class Leaderboard(Document):
    user = ReferenceField(User, required=True)
    score = IntField(required=True)

class Workout(Document):
    name = StringField(max_length=255, required=True)
    description = StringField()