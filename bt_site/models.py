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
    player_sports = MultiSelectField("Player Sports", choices = SPORTS_CHOICES, default='None')

    # sport skill levels
    basketball_skill_level = models.PositiveSmallIntegerField("Basketball Skill Level", default=0)
    soccer_skill_level = models.PositiveSmallIntegerField("Soccer Skill Level", default=0)
    softball_skill_level = models.PositiveSmallIntegerField("Softball Skill Level", default=0)

    # birthday
    player_birthday = models.DateField("Player Birthday", default=1/1/2000)

    # rating
    player_rating = models.DecimalField("Player Rating", max_digits=2, decimal_places=1, default=0)

    # location
    player_location = models.CharField("Player Location", max_length=30, default='None')

    # playing range
    player_distance_preference = models.PositiveSmallIntegerField("Playing Range", default=25)


    # #player_times_available =  # TODO: need to create table relating digits to times/days of week

    # player tags
    COMPETE = 'Comp.'
    SOCIAL = 'Soc.'
    GOALS_CHOICES = [
        (COMPETE, 'Competition'),
        (SOCIAL, 'Socializing'),
    ]
    player_tags = MultiSelectField("Player Tags", max_length=30, choices=GOALS_CHOICES, default="None")

    # player badges
    BADGE1 = 'Temp1'
    BADGE2 = 'Temp2'
    BADGE_CHOICES = [
        (BADGE1, 'Badge 1'),
        (BADGE2, 'Badge 2'),
    ]
    player_badges = MultiSelectField("Player Badges", max_length=30, choices=BADGE_CHOICES, default="None")


    # associated groups


    # associated people (friends)


    # past games

    
    # upcoming games


    def __str__(self):
        return self.player_first_name + self.player_last_name



class Group(models.Model):
    # name
    group_name = models.CharField("Group Name", max_length=30, default="None")

    # location
    group_location = models.CharField("Group Location", max_length=30, default="None")

    # description
    group_description = models.CharField("Group Description", max_length=200, default="None")

    # group type
    PUBLIC = 'Pub.'
    FRIENDS = 'Fr.'
    INVITE = 'Inv.'
    GROUP_TYPE_CHOICES = [
        (PUBLIC, 'Public'),
        (FRIENDS, 'Friends Only'),
        (INVITE, 'Invite Only'),
    ]
    group_type = models.CharField("Group Type", max_length=5, choices=GROUP_TYPE_CHOICES, default=PUBLIC)

    # rating
    group_rating = models.DecimalField("Group Rating", max_digits=2, decimal_places=1, default=0)


    # sports
    BASKETBALL = 'Bball'
    SOCCER = 'Soc.'
    SOFTBALL = 'Soft.'
    SPORTS_CHOICES = [
        (BASKETBALL, 'Basketball'),
        (SOCCER, 'Soccer'),
        (SOFTBALL, 'Softball'),
    ]
    group_sport = models.CharField("Group Sport", max_length=30, choices=SPORTS_CHOICES, default="None") # do we want to allow multisport groups?

    # skill level
    group_skill_level = models.PositiveSmallIntegerField("Group Skill Level", default = 3)

    # group size
    group_size = models.PositiveSmallIntegerField("Number of Members", default = 0)

    # group tags
    COMPETE = 'Comp.'
    SOCIAL = 'Soc.'
    GOALS_CHOICES = [
        (COMPETE, 'Competition'),
        (SOCIAL, 'Socializing'),
    ]
    group_goals = models.CharField("Group Tags", max_length=30, choices=GOALS_CHOICES, default=COMPETE)

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
    venue_rating = models.DecimalField("Venue Rating", max_digits=2, decimal_places=1, default=0)

    # available sports
    BASKETBALL = 'Bball'
    SOCCER = 'Soc.'
    SOFTBALL = 'Soft.'
    SPORTS_CHOICES = [
        (BASKETBALL, 'Basketball'),
        (SOCCER, 'Soccer'),
        (SOFTBALL, 'Softball'),
    ]
    venue_sports = MultiSelectField("Venue Sports", choices=SPORTS_CHOICES, default='None')

    # type
    CITY = 'City'
    SCHOOL = 'School'
    REC = 'Rec.'
    VENUE_TYPE_CHOICES = [
        (CITY, 'City Property'),
        (SCHOOL, 'School Property'),
        (REC, 'Rec. Facility')
    ]
    venue_type = models.CharField("Venue Type", max_length = 6, choices=VENUE_TYPE_CHOICES, default="None")

    # size/capacity
    venue_capacity = models.PositiveSmallIntegerField("Venue Capacity", default=0)

class Availability(models.Model):
    
    # id of relevant player/group/venue
    
    # day of week
    SUN = 'Sunday'
    MON = 'Monday'
    TUE = 'Tuesday'
    WED = 'Wednesday'
    THU = 'Thursday'
    FRI = 'Friday'
    SAT = 'Saturday'
    DAY_CHOICES = [
        (SUN, 'Sunday'),
        (MON, 'Monday'),
        (TUE, 'Tuesday'),
        (WED, 'Wednesday'),
        (THU, 'Thursday'),
        (FRI, 'Friday'),
        (SAT, 'Saturday')
    ]
    day = models.CharField("Day of Week", max_length = 9, choices=DAY_CHOICES, default="None")

    # hours
    open_time = models.TimeField("Opening Time")
    close_time = models.TimeField("Closing Time")
