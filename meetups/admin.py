from django.contrib import admin

# Models
from meetups.models import Meetup, Attendee, Talk, Sponsor


class MeetupAdmin(admin.ModelAdmin):
    model = Meetup

    filter_horizontal = ['attendees', 'talks', 'sponsors']

class AttendeeAdmin(admin.ModelAdmin):
    model = Attendee

    def full_name(obj):
        return "%s %s" % (obj.first_name, obj.last_name)

    list_display = [full_name, 'email', 'profession', 'python_exp']


# Register to admin 
admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Attendee, AttendeeAdmin)
admin.site.register(Talk)
admin.site.register(Sponsor)