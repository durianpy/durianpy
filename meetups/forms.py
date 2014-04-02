from django import forms
from meetups.models import Attendee


class AttendeeForm(forms.ModelForm):

    class Meta:
        model = Attendee