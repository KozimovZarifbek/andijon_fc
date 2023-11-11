from rest_framework import serializers
from .models import *

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "all"


class NavbarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navbar
        fields = "all"


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "all"


class Game_scheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game_schedule
        fields = "all"


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "all"


class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = "all"


class YoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Youtube
        fields = "all"


class Player_statisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player_statistics
        fields = "all"


class Shop_1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Shop_1
        fields = "all"


class Shop_2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Shop_2
        fields = "all"


class Shop_3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Shop_3
        fields = "all"


class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = "all"


class Stadium_photoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium_photo
        fields = "all"


class Arena_historySerializer(serializers.ModelSerializer):
    class Meta:
        model = Arena_history
        fields = "all"


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Arena_history2
        fields = "all"


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Arena_history3
        fields = "all"


class About_shopSerializer(serializers.ModelSerializer):
    class Meta:
        model = About_shop
        fields = "all"


class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = "all"


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = "all"


class Club_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club_info
        fields = "all"


class Club_historySerializer(serializers.ModelSerializer):
    class Meta:
        model = Club_history
        fields = "all"


class RecommendationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendations
        fields = "all"


class AcademySerializer(serializers.ModelSerializer):
    class Meta:
        model = Academy
        fields = "all"


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = "all"


class Bobur_arenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bobur_arena
        fields = "all"


class ManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = "all"


class Team_membersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team_members
        fields = "all"


class Arena_history2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Arena_history2
        fields = "all"


class Arena_history3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Arena_history3
        fields = "all"