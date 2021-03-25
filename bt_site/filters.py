import django_filters
from .models import UserProfile

class UserFilter(django_filters.FilterSet):
	class Meta:
		model = UserProfile
		#fields = ('age', 'desc')
		fields = {
			'age': ['icontains'],
			'desc': ['icontains'],
		}