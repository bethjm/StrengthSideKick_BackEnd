# Generated by Django 4.2.5 on 2023-09-25 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cues', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Stretch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('video', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('upper_body', 'Upper Body'), ('lower_body', 'Lower Body'), ('core', 'Core'), ('power', 'Power')], max_length=255)),
                ('subcategory', models.CharField(choices=[('default_option', 'Default Option'), ('vertical_push', 'Vertical Push'), ('horizontal_push', 'Horizontal Push'), ('vertical_pull', 'Vertical Pull'), ('horizontal_pull', 'Horizontal Pull'), ('knee_flexion', 'Knee Flexion'), ('hip_dominant', 'Hip Dominant'), ('knee_dominant', 'Knee Dominant'), ('side_abs', 'Side Abs'), ('low_abs', 'Low Abs'), ('knee_felxed_abs', 'Knee Flexed Abs'), ('locomotion_abs', 'Locomotion Abs'), ('power_lowerbody', 'Power Lower Body'), ('power_upperbody', 'Power Upper Body')], default='default_option', max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('experience_level', models.CharField(choices=[('novice', 'Novice'), ('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], max_length=255)),
                ('bi_or_uni', models.CharField(choices=[('unilateral', 'Unilateral'), ('bilateral', 'Bilateral')], max_length=255)),
                ('equipment', models.CharField(choices=[('kettlebell', 'Kettle Bell'), ('dumbell', 'Dumbell'), ('barbell', 'Barbell'), ('hexbar', 'Hex Bar'), ('ssb', 'SSB'), ('cable', 'Cable'), ('miniband', 'Mini Band'), ('bodyweight', 'Body Weight'), ('yogaball', 'Yoga Ball'), ('foamroller', 'Foam Roller'), ('pullup_bar', 'Pull up bar'), ('box', 'Box')], default='bodyweight', max_length=255)),
                ('video', models.URLField(blank=True)),
                ('exercise_cues', models.ManyToManyField(blank=True, related_name='cues_for_exercises', to='exercise_app.cue')),
            ],
        ),
        migrations.AddField(
            model_name='cue',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercise_app.exercise'),
        ),
    ]
