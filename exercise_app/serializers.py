from rest_framework import serializers
from .models import Cue, Exercise
#Stretch

class CueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cue
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

# class StretchSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Stretch
#         fields = '__all__'
