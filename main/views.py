from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

# Models
from meetups.models import Meetup



class IndexView(TemplateView):
    """
    DurianPy's Index Page
    """
    template_name = 'main/index.html'
    context = {}
    meetup_class = Meetup

    def get(self, request, *args, **kwargs):
        self.context['feed'] = self.meetup_class.objects.all().order_by('-event_date')
        return render(request, self.template_name, self.context)


class AboutView(TemplateView):
    """
    DurianPy's About Page
    """
    template_name = 'main/about.html'
    context = {}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)


class ContactView(TemplateView):
    """
    DurianPy's Contact Page
    """
    template_name = 'main/contact.html'
    context = {}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)