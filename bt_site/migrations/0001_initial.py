# Generated by Django 3.1.2 on 2021-05-07 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shuttle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shuttle_time_date', models.DateField(verbose_name='Date of Shuttle Ride')),
                ('shuttle_time', models.TimeField(verbose_name='Time of Shuttle Ride')),
                ('shuttle_availability', models.IntegerField(default=8)),
                ('shuttle_destination', models.CharField(choices=[('Route A: Bethpage State Park', 'Route A: Bethpage State Park'), ('Route B: Spook Rock/Darlington/New York Country Club', 'Route B: Spook Rock/Darlington/New York Country Club'), ('Route C: Soldier Hill/Valley Brook/Rockleigh', 'Route C: Soldier Hill/Valley Brook/Rockleigh'), ('Route D: Eisenhower State Park', 'Route D: Eisenhower State Park'), ('Route E: Pelham Bay/Split Rock', 'Route E: Pelham Bay/Split Rock'), ('Pelham Bay', 'Pelham Bay')], max_length=60, verbose_name='Golf Course')),
                ('is_full', models.BooleanField(default=False)),
                ('shuttle_price', models.DecimalField(decimal_places=2, default=100.0, max_digits=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_phone_number', models.CharField(blank=True, max_length=15, verbose_name='Phone Number')),
                ('user_neighborhood', models.CharField(blank=True, choices=[('Soho', 'Soho'), ('Tribeca', 'Tribeca')], max_length=20, verbose_name='Neighborhood')),
                ('user_handicap', models.CharField(choices=[('15+', '15+'), ('5-15', '5-15'), ('<5', '<5')], max_length=20, verbose_name='Handicap')),
                ('user_style', models.CharField(choices=[('Beer and Music', 'Beer and Music'), ('Fun but Focused', 'Fun but Focused'), ('Serious', 'Serious')], max_length=20, verbose_name='Style of Play')),
                ('user_pace', models.CharField(choices=[('Leisurely', 'Leisurely'), ('Average', 'Average'), ('Speedy', 'Speedy')], max_length=20, verbose_name='Pace of Play')),
                ('user_partners', models.CharField(choices=[('No interest', 'No interest'), ('Looking for casual playing partners', 'Looking for casual playing partners'), ('Looking for competitive playing partners', 'Looking for competitive playing partners')], max_length=45, verbose_name='Looking for playing partners?')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShuttleGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shuttle_group_date', models.DateField(verbose_name='Date of Shuttles Time')),
                ('shuttles', models.ManyToManyField(related_name='shuttle_time_group', to='bt_site.Shuttle')),
            ],
        ),
        migrations.AddField(
            model_name='shuttle',
            name='shuttle_potential_users',
            field=models.ManyToManyField(related_name='tee_time_potential_users', to='bt_site.UserProfile'),
        ),
        migrations.AddField(
            model_name='shuttle',
            name='shuttle_users',
            field=models.ManyToManyField(related_name='shuttle_time_users', to='bt_site.UserProfile'),
        ),
    ]
