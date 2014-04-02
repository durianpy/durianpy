from django.contrib import admin

# Models
from meetups.models import Meetup, Attendee


class MeetupAdmin(admin.ModelAdmin):
    model = Meetup

    filter_horizontal = ['attendees']

class AttendeeAdmin(admin.ModelAdmin):
    model = Attendee


# Register to admin 
admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Attendee, AttendeeAdmin)