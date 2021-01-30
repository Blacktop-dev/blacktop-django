from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.forms import *

# Create your models here.

class Player(models.Model):
    # name
    player_first_name = models.CharField("First Name", max_length=30, default='First')
    player_last_name = models.CharField("Last Name", max_length=30, default='Last')

    # player_id

    # email
    player_email = models.EmailField("Email", default='example@host.com')

    # phone number
    player_phone_number = models.CharField("Phone Number", max_length=30, default='(xxx) xxx-xxxx')

    # gender
    MALE = 'M'
    FEMALE = 'F'
    NONBINARY = 'Non'
    OTHER = 'O'
    NOTSAY = 'NA'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NONBINARY, 'Non-binary'),
        (OTHER, 'Other'),
        (NOTSAY, 'Prefer not to say')
    ]
    player_gender = models.CharField("Gender", max_length=30, choices=GENDER_CHOICES, default='None')

    # sports played
    BASKETBALL = 'Bball'
    SOCCER = 'Soc.'
    SOFTBALL = 'Soft.'
    SPORTS_CHOICES = [
        (BASKETBALL, 'Basketball'),
        (SOCCER, 'Soccer'),
        (SOFTBALL, 'Softball'),
    ]
    player_sports = MultiSelectField(choices = SPORTS_CHOICES, default='None')

    # sport skill levels
    basketball_skill_level = models.PositiveSmallIntegerField("Basketball Skill Level", default="None")
    soccer_skill_level = models.PositiveSmallIntegerField("Soccer Skill Level", default="None")
    softball_skill_level = models.PositiveSmallIntegerField("Softball Skill Level", default="None")

    # birthday
    player_birthday = models.DateField("Birthday", default=1/1/2000)

    # rating
    player_rating = models.DecimalField("Rating", max_digits=2, decimal_places=1, default=0)

    # location
    player_location = models.CharField("Location", max_length=30, default='None')

    # playing range
    player_distance_preference = models.PositiveSmallIntegerField("Playing Range", default=25)


    #player_times_available =  # TODO: need to create table relating digits to times/days of week

    # player tags
    COMPETE = 'Comp.'
    SOCIAL = 'Soc.'
    GOALS_CHOICES = [
        (COMPETE, 'Competition'),
        (SOCIAL, 'Socializing'),
    ]
    player_tags = MultiSelectField("Playing Goals", max_length=30, choices=GOALS_CHOICES)

    # player badges
    BADGE1 = 'Temp1'
    BADGE2 = 'Temp2'
    BADGE_CHOICES = [
        (BADGE1, 'Badge 1'),
        (BADGE2, 'Badge 2'),
    ]

    # associated groups


    # associated people (friends)


    # past games

    
    # upcoming games



    def __str__(self):
        return self.player_first_name + self.player_last_name

class Group(models.Model):
    # name
    group_name = models.CharField("Group Name", max_length=30)

    # location
    group_location = models.CharField("Group Location", max_length=30)

    # description
    group_description = models.CharField("Group Description", max_length=200, default="None")

    # group type
    PUBLIC = 'Pub.'
    FRIENDS = 'Fr.'
    INVITE = 'Inv.'
    GROUP_TYPE_CHOICES = [
        (PUBLIC, 'Public'),
        (FRIENDS, 'Friends of Group Members'),
        (INVITE, 'Invite by Group Members Only')
    ]

    # rating
    player_rating = models.DecimalField("Rating", max_digits=2, decimal_places=1, default=0)

    # sports
    BASKETBALL = 'Bball'
    SOCCER = 'Soc.'
    SOFTBALL = 'Soft.'
    SPORTS_CHOICES = [
        (BASKETBALL, 'Basketball'),
        (SOCCER, 'Soccer'),
        (SOFTBALL, 'Softball'),
    ]
    group_sport = models.CharField("Group Sport", max_length=30, choices=SPORTS_CHOICES) # do we want to allow multisport groups?

    # skill level
    group_skill_level = models.PositiveSmallIntegerField("Group Skill Level")

    # group size
    group_size = models.PositiveSmallIntegerField("Number of Members")

    # group tags
    COMPETE = 'Comp.'
    SOCIAL = 'Soc.'
    GOALS_CHOICES = [
        (COMPETE, 'Competition'),
        (SOCIAL, 'Socializing'),
    ]
    group_goals = models.CharField("Playing Goals", max_length=30, choices=GOALS_CHOICES)


    # group members



    


    def __str__(self):
        return self.group_name

class Venue(models.Model):
    # name
    venue_name = models.CharField("Venue Name", max_length=50, default="None")

    # info
    venue_info = models.CharField("Venue Info", max_length=200, default="None")

    # address
    venue_street_address = models.CharField("Street Address", max_length=50, default="None")
    venue_city = models.CharField(max_length=30, default="None")
    venue_state = USStateField()
    venue_zip = USZipCodeField()

    # hours

    # rating

    # available sports

    # type

    # size/capacity
