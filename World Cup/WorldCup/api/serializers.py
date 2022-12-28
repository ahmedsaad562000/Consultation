
from curses import meta


from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from accounts.models import User
from matches.models import Stadiums , Matches , Teams , Tickets , Refrees
from django.db import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['id','username','first_name','last_name','email','role','nationality']

class StadiumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadiums
        fields=['name','rows','seats_per_row','link','description']

class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields=['name']

class TeamslinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields=['link']

class RefreesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refrees
        fields=['name']

class MatchesSerializer(serializers.ModelSerializer):
    h_team_link = TeamslinkSerializer(source='h_team', many=False)
    a_team_link = TeamslinkSerializer(source='a_team', many=False)
    class Meta:
        model = Matches

        fields=['id' , 'date' ,'time' ,'h_team' ,'h_team_link','a_team' ,'a_team_link' ,'ref' ,'line1' ,'line2' , 'stadium']

class Tickets_print_Serializer(serializers.ModelSerializer):
        h_team = serializers.CharField(source='Matches.h_team');
        a_team = serializers.CharField(source='Matches.a_team');
        stadium = serializers.CharField(source='Matches.stadium');  
        date = serializers.DateField(source='Matches.date');
        time = serializers.TimeField(source='Matches.time');
        
        class Meta:
            model = Tickets
            fields = ['id' ,'h_team' , 'a_team' , 'stadium' ,'date' ,'time','row','seat']

class Tickets_add_Serializer(serializers.ModelSerializer):
        class Meta:
            model = Tickets
            fields = ['match' , 'user' ,'row','seat']



            