import datetime
from django.db import models



class Meetup(models.Model):

    title = models.CharField(max_length=255)
    event_date = models.DateTimeField(default=datetime.datetime.now())
    location = models.TextField(null=True, blank=True)
    event_type = models.CharField(max_length=200, null=True, blank=True, default="Meetup")

    description = models.TextField(null=True, blank=True)

    talks = models.ManyToManyField('Talk', null=True, blank=True)
    attendees = models.ManyToManyField('Attendee', null=True, blank=True)
    sponsors = models.ManyToManyField('Sponsor', null=True, blank=True)

    active = models.BooleanField(default=False)
    limit = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return "%s" % self.title

    def get_available_tickets(self):
        total = self.limit - self.attendees.all().count()
        return "%s" % total


class Talk(models.Model):

    title = models.CharField(max_length=255)
    speaker = models.CharField(max_length=200)
    profession = models.CharField(max_length=200, null=True, blank=True)
    image = models.FileField(upload_to="speakers/", null=True, blank=True)
    handle = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.title


class Sponsor(models.Model):

    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.name


class Attendee(models.Model):

    NO_EXPERIENCE = "0"
    BEGINNER = "1"
    INTERMEDIATE = "2"
    EXPERT = "3"

    STATUS = (
        (NO_EXPERIENCE, 'No Experience'),
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (EXPERT, 'Expert')
    )

    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    profession = models.CharField(max_length=75, null=True, blank=True)
    email = models.CharField(max_length=75, null=True, blank=True)
    python_exp = models.CharField(max_length=20, choices=STATUS, default=NO_EXPERIENCE)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)
