from django.urls import path

#old
from . import views

#new
# from .views import ListCues, ListExercises
# ListStretches


urlpatterns = [
# old
path('', views.ListExercises.as_view()),

#new
    # path('cues/', ListCues.as_view(), name='list_cues'),
    # path('exercises/', ListExercises.as_view(), name='list_exercises'),
    # path('stretches/', ListStretches.as_view(), name='list_stretches'),
]