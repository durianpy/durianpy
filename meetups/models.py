import datetime
from django.db import models



class Meetup(models.Model):

    title = models.CharField(max_length=255)
    event_date = models.DateTimeField(default=datetime.datetime.now())
    location = models.TextField(null=True, blank=True)

    description = models.TextField(null=True, blank=True)

    attendees = models.ManyToManyField('Attendee', null=True, blank=True)
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s" % self.title


class Attendee(models.Model):

    # STUDENT = 'student'
    # PROFESSIONAL = 'professional'
    # OTHER = 'other'

    # STATUS = (
    #     (STUDENT, 'Student'),
    #     (PROFESSIONAL, 'Professional'),
    #     (OTHER, 'Other'),
    # )

    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    profession = models.CharField(max_length=75, null=True, blank=True)
    email = models.CharField(max_length=75, null=True, blank=True)
    #status = models.CharField(max_length=20, choices=STATUS)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)