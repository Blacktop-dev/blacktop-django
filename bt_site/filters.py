import django_filters
from .models import UserProfile, Shuttle

class UserFilter(django_filters.FilterSet):
	class Meta:
		model = UserProfile
		fields = {
			'user_neighborhood': ['icontains']
			# 'age': ['icontains'],
			# 'user_sports': ['icontains'],
			# 'user_location': ['icontains'],
			# 'user_tags': ['icontains']
			# 'user_gender': ['icontains']
		}

class TeeTimeFilter(django_filters.FilterSet):
	class Meta:
		model = Shuttle
		fields = {
			'shuttle_destination': ['icontains']
		}