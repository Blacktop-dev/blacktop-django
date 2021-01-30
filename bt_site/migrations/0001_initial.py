# Generated by Django 3.1.5 on 2021-01-30 03:50

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=30, verbose_name='Group Name')),
                ('group_location', models.CharField(max_length=30, verbose_name='Group Location')),
                ('group_description', models.CharField(default='None', max_length=200, verbose_name='Group Description')),
                ('player_rating', models.DecimalField(decimal_places=1, default=0, max_digits=2, verbose_name='Rating')),
                ('group_sport', models.CharField(choices=[('Bball', 'Basketball'), ('Soc.', 'Soccer'), ('Soft.', 'Softball')], max_length=30, verbose_name='Group Sport')),
                ('group_skill_level', models.PositiveSmallIntegerField(verbose_name='Group Skill Level')),
                ('group_size', models.PositiveSmallIntegerField(verbose_name='Number of Members')),
                ('group_goals', models.CharField(choices=[('Comp.', 'Competition'), ('Soc.', 'Socializing')], max_length=30, verbose_name='Playing Goals')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_first_name', models.CharField(default='First', max_length=30, verbose_name='First Name')),
                ('player_last_name', models.CharField(default='Last', max_length=30, verbose_name='Last Name')),
                ('player_email', models.EmailField(default='example@host.com', max_length=254, verbose_name='Email')),
                ('player_phone_number', models.CharField(default='(xxx) xxx-xxxx', max_length=30, verbose_name='Phone Number')),
                ('player_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Non', 'Non-binary'), ('O', 'Other'), ('NA', 'Prefer not to say')], default='None', max_length=30, verbose_name='Gender')),
                ('player_sports', multiselectfield.db.fields.MultiSelectField(choices=[('Bball', 'Basketball'), ('Soc.', 'Soccer'), ('Soft.', 'Softball')], default='None', max_length=16)),
                ('basketball_skill_level', models.PositiveSmallIntegerField(default='None', verbose_name='Basketball Skill Level')),
                ('soccer_skill_level', models.PositiveSmallIntegerField(default='None', verbose_name='Soccer Skill Level')),
                ('softball_skill_level', models.PositiveSmallIntegerField(default='None', verbose_name='Softball Skill Level')),
                ('player_birthday', models.DateField(default=0.0005, verbose_name='Birthday')),
                ('player_rating', models.DecimalField(decimal_places=1, default=0, max_digits=2, verbose_name='Rating')),
                ('player_location', models.CharField(default='None', max_length=30, verbose_name='Location')),
                ('player_distance_preference', models.PositiveSmallIntegerField(default=25, verbose_name='Playing Range')),
                ('player_tags', multiselectfield.db.fields.MultiSelectField(choices=[('Comp.', 'Competition'), ('Soc.', 'Socializing')], max_length=30, verbose_name='Playing Goals')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_name', models.CharField(default='None', max_length=50, verbose_name='Venue Name')),
                ('venue_info', models.CharField(default='None', max_length=200, verbose_name='Venue Info')),
                ('venue_street_address', models.CharField(default='None', max_length=50, verbose_name='Street Address')),
                ('venue_city', models.CharField(default='None', max_length=30)),
            ],
        ),
    ]