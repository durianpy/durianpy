from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

# Models
from meetups.models import Meetup

# Forms
from meetups.forms import AttendeeForm


class MeetupView(TemplateView):
    template_name = 'meetups/meetup.html'
    context = {}
    meetup = Meetup

    def get(self, *args, **kwargs):
        # Load active meetup
        self.context['meetup'] = self.get_active_meetup()

        return render(self.request, self.template_name, self.context)

    def get_active_meetup(self):
        return self.meetup.objects.get(active=True)


class RegisterView(TemplateView):
    template_name = 'meetups/attendee.html'
    context = {}
    meetup = Meetup
    form_class = AttendeeForm
    meetup_view = MeetupView()

    def get(self, *args, **kwargs):
        # load form
        self.context['form'] = self.form_class()
        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            attendee = form.save()

            # Add to the active meetup
            self.update_attendees(attendee)

            return HttpResponseRedirect(reverse('meetup'))

        self.context['form'] = form
        return render(self.request, self.template_name, self.context)

    def update_attendees(self, attendee):
            meetup = self.meetup_view.get_active_meetup()
            meetup.attendees.add(attendee)
            meetup.save()

