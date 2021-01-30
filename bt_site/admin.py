from django.contrib import admin

# Register your models here.

from bt_site.models import Player, Group, Venue

admin.site.register(Player)
admin.site.register(Group)
admin.site.register(Venue)