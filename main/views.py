from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView



class IndexView(TemplateView):
    """
    DurianPy's Index Page
    """
    template_name = 'main/index.html'
    context = {}

    def get(self, request, *args, **kwargs):
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