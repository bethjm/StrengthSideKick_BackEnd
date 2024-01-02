from rest_framework import generics
from .models import Cue, Exercise
#Stretch
from .serializers import CueSerializer, ExerciseSerializer
#StretchSerializer

class ListCues(generics.ListAPIView):
    queryset = Cue.objects.all()
    serializer_class = CueSerializer

class ListExercises(generics.ListAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

# class ListStretches(generics.ListAPIView):
#     queryset = Stretch.objects.all()
#     serializer_class = StretchSerializer
