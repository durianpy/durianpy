from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, FormView

# Models
from meetups.models import Meetup

# Forms
from meetups.forms import AttendeeForm


class MeetupView(FormView):
    template_name = 'meetups/meetup.html'
    context = {}
    form_class = AttendeeForm
    meetup = Meetup

    def get(self, *args, **kwargs):
        self.context['meetup'] = self.get_meetup(kwargs['meetup_id'])
        self.context['form'] = self.form_class()

        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            attendee = form.save()
            
            # Add attendee to meetup
            meetup = self.get_meetup(kwargs['meetup_id'])
            meetup.attendees.add(attendee)
            meetup.save()

            return HttpResponseRedirect(reverse('meetup', args=[meetup.id]))

        self.context['form'] = form
        return render(self.request, self.template_name, self.context)



    def get_meetup(self, meetup_id):
        return self.meetup.objects.get(id=meetup_id)

