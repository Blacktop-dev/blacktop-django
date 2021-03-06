from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField
from datetime import date

### OPTION DEFINITIONS ###

# neighborhoods
SOHO = 'Soho'
TRIBECA = 'Tribeca'
NEIGHBORHOOD_CHOICES = [
    (SOHO, 'Soho'),
    (TRIBECA, 'Tribeca')
]

# courses
PELHAM = 'Pelham Bay'
COURSE_CHOICES = [
    (PELHAM, 'Pelham Bay')
]


class UserProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    user_phone_number = models.CharField('Phone Number', max_length=15, blank=True)
    user_neighborhood = models.CharField('Neighborhood', max_length=20, choices=NEIGHBORHOOD_CHOICES, blank=True)
    # user_tee_times = models.ManyToManyField(related_name='bt_site.tee_time_users')


#can do something wtih the tea time object sending stuff with the request
class TeeTime(models.Model):
    #TODO: should probs change this to User instead of UserProfile bc cases were UserProfile does not exist
    #tee_time_users = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    #tee_time_users = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    #tee_time_users = models.ManyToManyField('UserProfile', blank=True, null=False, related_name='user_tee_times')
    #tee_time_users = models.ManyToManyField('UserProfile', blank=True, null=False, related_name='user_tee_times')
    #tee_time_users = models.ManyToManyField('UserProfile', related_name='user_tee_times')
    tee_time_users = models.ManyToManyField('UserProfile', related_name='tee_time_users')
    tee_time_potential_users = models.ManyToManyField('UserProfile', related_name='tee_time_potential_users')
    tee_time_date = models.DateField('Date of Tee Time')
    tee_time_course = models.CharField('Golf Course', max_length=30, choices=COURSE_CHOICES)

class TeeTimeGroup(models.Model):
    tee_group_members = models.ManyToManyField('TeeTime', related_name='tee_time_group')
    tee_group_date = models.DateField('Date of Tee Time')