from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.forms import *

### OPTION DEFINITIONS ###

# player gender
MALE = 'Male'
FEMALE = 'Female'
NONBINARY = 'Non-Binary'
OTHER = 'Other'
NOTSAY = 'Prefer not to say'
PLAYER_GENDER_CHOICES = [
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (NONBINARY, 'Non-binary'),
    (OTHER, 'Other'),
    (NOTSAY, 'Prefer not to say')
]

# game/group gender
MALE = 'Male'
FEMALE = 'Female'
COED = 'Coed'
GENDER_CHOICES = [
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (COED, 'Coed')
]

# sports
BASKETBALL = 'Basketball'
SOCCER = 'Soccer'
SOFTBALL = 'Softball'
SPORTS_CHOICES = [
    (BASKETBALL, 'Basketball'),
    (SOCCER, 'Soccer'),
    (SOFTBALL, 'Softball')
]

# skill level
BEGINNER = 'Beginner'
NOVICE = 'Novice'
INTERMEDIATE = 'Intermediate'
ADVANCED = 'Advanced'
EXPERT = 'Expert'
SKILL_CHOICES = [
    (BEGINNER, 'Beginner'),
    (NOVICE, 'Novice'),
    (INTERMEDIATE, 'Intermediate'),
    (ADVANCED, 'Advanced'),
    (EXPERT, 'Expert')
]

# playing tags/goals
COMPETITION = 'Competition'
SOCIALIZING = 'Socializing'
EXERCISE = 'Exercise'
IMPROVEMENT = 'Improvement'
GOALS_CHOICES = [
    (COMPETITION, 'Competition'),
    (SOCIALIZING, 'Socializing'),
    (EXERCISE, 'Exercise'),
    (IMPROVEMENT, 'Improvement')
]

# badges
BADGE1 = 'Temp1'
BADGE2 = 'Temp2'
BADGE_CHOICES = [
    (BADGE1, 'Badge 1'),
    (BADGE2, 'Badge 2')
]

# group type
PUBLIC = 'Public'
FRIENDS = 'Friends Only'
INVITE = 'Invite Only'
GROUP_TYPE_CHOICES = [
    (PUBLIC, 'Public'),
    (FRIENDS, 'Friends Only'),
    (INVITE, 'Invite Only')
]

# venue type
CITY = 'City Property'
SCHOOL = 'School Property'
REC = 'Rec. Facility'
VENUE_TYPE_CHOICES = [
    (CITY, 'City Property'),
    (SCHOOL, 'School Property'),
    (REC, 'Rec. Facility')
]

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

# game type
CASUAL = 'Casual'
COMPETITIVE = 'Competitive'
GAME_TYPE_CHOICES = [
    (CASUAL, 'Casual'),
    (COMPETITIVE, 'Competitive')
]



class Player(models.Model):

    # player id
    player_id = models.AutoField(primary_key=True)

    # name
    player_first_name = models.CharField("First Name", max_length=30, default='First')
    player_last_name = models.CharField("Last Name", max_length=30, default='Last')

    # email
    player_email = models.EmailField("Email", default='example@host.com')

    # phone number
    player_phone_number = models.CharField("Phone Number", max_length=30, default='(xxx) xxx-xxxx')

    # gender
    player_gender = models.CharField("Gender", max_length=30, choices=PLAYER_GENDER_CHOICES, default='None')

    # sports played
    player_sports = MultiSelectField("Player Sports", choices = SPORTS_CHOICES, default='None')

    # sport skill levels
    basketball_skill_level = models.CharField("Basketball Skill Level", max_length=12, choices=SKILL_CHOICES, blank=True)
    soccer_skill_level = models.CharField("Soccer Skill Level", max_length=12, choices=SKILL_CHOICES, blank=True)
    softball_skill_level = models.CharField("Softball Skill Level", max_length=12, choices=SKILL_CHOICES, blank=True)

    # birthday
    player_birthday = models.DateField("Player Birthday", default=1/1/2000)

    # rating
    player_rating = models.DecimalField("Player Rating", max_digits=2, decimal_places=1, default=0)

    # location
    player_location = models.CharField("Player Location", max_length=30, default='None')

    # playing range
    player_distance_preference = models.PositiveSmallIntegerField("Playing Range", default=25)

    # player tags
    player_tags = MultiSelectField("Player Tags", max_length=30, choices=GOALS_CHOICES, default="None")

    # player badges
    player_badges = MultiSelectField("Player Badges", max_length=30, choices=BADGE_CHOICES, default="None")

    # associated groups
    player_groups = models.ManyToManyField('Group', related_name='player_groups')

    # associated people (friends)
    player_friends = models.ManyToManyField('self', related_name='player_friends')

    # past games
    player_past_games = models.ManyToManyField('Game', related_name='player_past_games')
    
    # upcoming games
    player_upcoming_games = models.ManyToManyField('Game', related_name='player_upcoming_games')


    def __str__(self):
        return self.player_first_name + self.player_last_name

class Group(models.Model):

    # group id
    group_id = models.AutoField(primary_key=True)

    # name
    group_name = models.CharField("Group Name", max_length=30, default="None")

    # location
    group_location = models.CharField("Group Location", max_length=30, default="None")

    # description
    group_description = models.CharField("Group Description", max_length=200, default="None")

    # group type
    group_type = models.CharField("Group Type", max_length=12, choices=GROUP_TYPE_CHOICES, default=PUBLIC)

    # rating
    group_rating = models.DecimalField("Group Rating", max_digits=2, decimal_places=1, default=0)

    # sports
    group_sport = models.CharField("Group Sport", max_length=30, choices=SPORTS_CHOICES, default="None") # do we want to allow multisport groups? I vote no

    # skill level
    group_skill_level = models.CharField("Group Skill Level", max_length=12, choices=SKILL_CHOICES, blank=True)

    # group size
    group_size = models.PositiveSmallIntegerField("Number of Members", default = 0)

    # group tags
    group_tags = models.CharField("Group Tags", max_length=30, choices=GOALS_CHOICES, default="None")

    # group gender
    group_gender = models.CharField("Group Gender", max_length=10, choices=GENDER_CHOICES, default = COED)

    # group members
    group_members = models.ManyToManyField('Player', related_name='group_members')


    def __str__(self):
        return self.group_name

class Venue(models.Model):

    # venue id
    venue_id = models.AutoField(primary_key=True)

    # name
    venue_name = models.CharField("Venue Name", max_length=50, default="None")

    # info
    venue_info = models.CharField("Venue Info", max_length=200, default="None")

    # address
    venue_street_address = models.CharField("Street Address", max_length=50, default="None")
    venue_city = models.CharField(max_length=30, default="None")
    venue_state = USStateField()
    venue_zip = USZipCodeField()

    # rating
    venue_rating = models.DecimalField("Venue Rating", max_digits=2, decimal_places=1, default=0)

    # available sports
    venue_sports = MultiSelectField("Venue Sports", choices=SPORTS_CHOICES, default='None')

    # type
    venue_type = models.CharField("Venue Type", max_length = 15, choices=VENUE_TYPE_CHOICES, default="None")

    # size/capacity
    venue_capacity = models.PositiveSmallIntegerField("Venue Capacity", default=0)

class Availability(models.Model):
    
    # player foreign key
    player = models.ManyToManyField(Player, related_name='player_availability', blank=True)

    # group foreign key
    group = models.ManyToManyField(Group, related_name='group_availability', blank=True)

    # venue foreign key
    venue = models.ManyToManyField(Venue, related_name='venue_availability', blank=True)

    # day of week
    day = models.CharField("Day of Week", max_length = 9, choices=DAY_CHOICES, default="None")

    # hours
    open_time = models.TimeField("Opening Time")
    close_time = models.TimeField("Closing Time")

class Game(models.Model):

    # game id
    game_id = models.AutoField(primary_key=True)

    # game name
    game_name = models.CharField("Game Name", max_length=50, default="None")

    # final game time
    game_time_final = models.DateTimeField("Finalized Game Date/Time", auto_now_add=True, blank=True)

    # game time options

    # game time vote

    # game type
    game_type = models.CharField("Game Type", max_length=11, choices=GAME_TYPE_CHOICES, default = CASUAL)

    # game skill level
    game_skill_level = models.CharField("Game Skill Level", max_length=12, choices=SKILL_CHOICES, blank=True)

    # game sport
    game_sport = models.CharField("Game Sport", max_length=10, choices=SPORTS_CHOICES, default="None")

    # game RSVPs
    player_RSVPs = models.ManyToManyField('Player', related_name='game_RSVPs') # M-M field, each player can RSVP to many games and each game 
                                                                                 # has RSVPs from many players

    # game fee
    game_fee = models.PositiveSmallIntegerField("Game Fee", default=0)

    # game venue
    venue = models.ForeignKey('Venue', related_name='game_venue', on_delete=models.CASCADE, default=1) # 1-M field, 1 venue can have many games but each game only has 1 venue

    # game gender
    game_gender = models.CharField('Game Gender', max_length=10, choices=GENDER_CHOICES, default=COED)

    # game host
    host_player = models.ForeignKey('Player', related_name='host_player', on_delete=models.CASCADE, blank=True, default=1) # 1-M fields, 1 player/group can host many
    host_group = models.ForeignKey('Group', related_name='host_group', on_delete=models.CASCADE, blank=True, default=1)    # games but each game can only have 1 host

    # game participants - different from RSVPs because this is who actually shows up, we can compare to RSVPs to determine reliability rating
    participants = models.ManyToManyField('Player', related_name='game_participants') # M-M field, each player can participate in many games and each game
                                                                                      # has many players participate

