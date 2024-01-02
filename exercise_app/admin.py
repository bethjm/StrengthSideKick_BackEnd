from django.contrib import admin
from .models import Cue, Exercise
# Stretch

class CueAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'id')  # Customize the displayed fields in the admin list view

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'subcategory', 'experience_level', 'bi_or_uni', 'equipment')
    list_filter = ('category', 'subcategory', 'experience_level', 'bi_or_uni', 'equipment')
    search_fields = ('name', 'category', 'subcategory')
    filter_horizontal = ('exercise_cues',)  # If you want to use a horizontal filter for the exercise_cues field
    # You can further customize the admin view for Exercise by adding more options here

# class StretchAdmin(admin.ModelAdmin):
#     list_display = ('name', 'category')

# Register your models and custom admin classes
admin.site.register(Cue, CueAdmin)
admin.site.register(Exercise, ExerciseAdmin)
# admin.site.register(Stretch, StretchAdmin)
