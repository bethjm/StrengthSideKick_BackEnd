from django.db import models
from multiselectfield import MultiSelectField


class Cue(models.Model):
    exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE)
    information = models.CharField(max_length=255, default="Take it slow.")

    def __str__(self):
        return f"{self.exercise.name} - Information: {self.information} Le Cues"

class Exercise(models.Model):
    UPPER_BODY_POSTERIOR = 'upper_body_posterior'
    UPPER_BODY_ANTERIOR = 'upper_body_anterior'
    LOWER_BODY_POSTERIOR = 'lower_body_posterior'
    LOWER_BODY_ANTERIOR = 'lower_body_anterior'
    CORE = 'core'
    POWER = 'power'
    CATEGORY_CHOICES = [
        (UPPER_BODY_POSTERIOR, 'Posterior Upper Body'),
        (UPPER_BODY_ANTERIOR, "Anterior Upper Body"),
        (LOWER_BODY_POSTERIOR, 'Posterior Lower Body'),
        (LOWER_BODY_ANTERIOR, 'Anterior Lower Body'),
        (CORE, 'Core'),
        (POWER, 'Power'),
    ]

    DEFAULT_OPTION = 'default_option'
    VERTICAL_PUSH = 'vertical_push'
    HORIZONTAL_PUSH = 'horizontal_push'
    VERTICAL_PULL = 'vertical_pull'
    HORIZONTAL_PULL = 'horizontal_pull'
    KNEE_FLEXION = 'knee_flexion'
    HIP_DOMINANT = 'hip_dominant'
    KNEE_DOMINANT = 'knee_dominant'
    SIDE_ABS = 'side_abs'
    LOW_ABS = 'low_abs'
    KNEE_FLEXED_ABS = 'knee_felxed_abs'
    LOCOMOTION_ABS = 'locomotion_abs'
    POWER_LOWERBODY = 'power_lowerbody'
    POWER_UPPERBODY = 'power_upperbody'
    SUB_CATEGORY_CHOICES = [
        (DEFAULT_OPTION, 'Default Option'),
        (VERTICAL_PUSH, 'Vertical Push'),
        (HORIZONTAL_PUSH, 'Horizontal Push'),
        (VERTICAL_PULL, 'Vertical Pull'),
        (HORIZONTAL_PULL, 'Horizontal Pull'),
        (KNEE_FLEXION, 'Knee Flexion'),
        (HIP_DOMINANT, 'Hip Dominant'),
        (KNEE_DOMINANT, 'Knee Dominant'),
        (SIDE_ABS, 'Side Abs'),
        (LOW_ABS, 'Low Abs'),
        (KNEE_FLEXED_ABS, 'Knee Flexed Abs'),
        (LOCOMOTION_ABS, 'Locomotion Abs'),
        (POWER_LOWERBODY, 'Power Lower Body'),
        (POWER_UPPERBODY, 'Power Upper Body'),
    ]

    NOVICE = 'novice'
    BEGINNER = 'beginner'
    INTERMEDIATE = 'intermediate'
    ADVANCED = 'advanced'
    EXPERIENCE_CHOICES = [
        (NOVICE, 'Novice'),
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
            ]

    UNILATERAL = 'unilateral'
    BILATERAL = 'bilateral'
    BIORUNI_CHOICES = [
        (UNILATERAL, 'Unilateral'),
        (BILATERAL, 'Bilateral'),
    ]

    KETTLEBELL = 'kettlebell'
    DUMBELL = 'dumbell'
    BARBELL = 'barbell'
    HEXBAR = 'hexbar'
    SSB = 'ssb'
    CABLE = 'cable'
    MINIBAND = 'miniband'
    BODYWEIGHT = 'bodyweight'
    YOGABALL ='yogaball'
    FOAMROLLER = 'foamroller'
    PULLUP_BAR = 'pullup_bar'
    BOX = 'box'
    BAR = 'bar'
    EQUIPMENT_CHOICES = [
        (KETTLEBELL, 'Kettle Bell'),
        (DUMBELL, 'Dumbell'),
        (BARBELL, 'Barbell'),
        (HEXBAR, 'Hex Bar'),
        (SSB, 'SSB'),
        (CABLE, 'Cable'),
        (MINIBAND, 'Mini Band'),
        (BODYWEIGHT, 'Body Weight'),
        (YOGABALL, 'Yoga Ball'),
        (FOAMROLLER, 'Foam Roller'),
        (PULLUP_BAR, 'Pull up bar'),
        (BOX, 'Box'),
        (BAR, 'Bar')
    ]

    GENERAL_FITNESS = 'general_fitness'
    BALANCE = 'balance'
    POSTURE = 'posture'
    STRENGTH = 'strength'
    PUSHUP = 'push_up'
    PULLUP = 'pull_up'
    SINGLE_LEG_SQUAT = 'single_leg_squat'
    SQUAT = 'squat'
    BUILD_BACK = 'build_back'
    BUILD_LOWER = 'build_lower'
    HIKE = 'hike'
    CLIMB = 'climb'
    CYCLE = 'cycle'
    HILL_CLIMB_CYCLE = 'hill_climb_cycle'
    RUN = 'run'
    GOAL_CHOICES = [
        (GENERAL_FITNESS, 'General Fitness'),
        (BALANCE, 'Balance'),
        (POSTURE, 'Posture'),
        (STRENGTH, 'Strength'),
        (PUSHUP, 'First Push up'),
        (PULLUP, 'First Pull up'),
        (SINGLE_LEG_SQUAT, 'Single Leg Squat'),
        (SQUAT, 'Squat'),
        (BUILD_BACK , 'Build Upper Body Muscle'),
        (BUILD_LOWER, 'Build Lower Body Muscle'),
        (HIKE, 'Hike'),
        (CLIMB, 'Climb'),
        (CYCLE, 'Cycle'),
        (HILL_CLIMB_CYCLE, 'Hill Climb Cycling'),
        (RUN, 'Run'),
    ]

    NARROW_ISA = 'narrow_isa'
    WIDE_ISA = 'wide_isa'
    BOTH = 'both'
    ISA_CHOICES = [
        (WIDE_ISA, 'Wide ISA'),
        (NARROW_ISA, 'Narrow ISA'),
        (BOTH, 'Both')
    ]

    GYM = 'gym'
    HOME = 'home'
    BODYWEIGHT = 'bodyweight'
    LOCATION_CHOICES = [
        (GYM, 'Gym'),
        (HOME, 'Home'),
        (BODYWEIGHT, 'Body weight only workout')
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, blank=False, null=False)
    subcategory = models.CharField(max_length=255, choices=SUB_CATEGORY_CHOICES, blank=False, null=False)
    fitness_goal = MultiSelectField(max_length=255, choices=GOAL_CHOICES, blank=False, null=False)
    can_be_warmup = models.BooleanField(default=False)
    experience_level = MultiSelectField(max_length=255, choices=EXPERIENCE_CHOICES, blank=False, null=False)
    workout_location = MultiSelectField(max_length=255, choices=LOCATION_CHOICES, default=GYM, blank=False, null=False)
    bi_or_uni = models.CharField(max_length=255, choices=BIORUNI_CHOICES, blank=False, null=False)
    isa = MultiSelectField(max_length=255, choices=ISA_CHOICES, blank=False, null=False, default=BOTH)
    equipment = models.CharField(max_length=255, choices=EQUIPMENT_CHOICES, default=BODYWEIGHT, blank=False, null=False)
    video = models.URLField(blank=False, null=False)
    exercise_cues = models.ManyToManyField(Cue, blank=True, related_name='cues_for_exercises')

    # maybe add in categories for increased challenge level and decreased challenge level. have it as a linked list?

    def __str__(self):
        return self.name
