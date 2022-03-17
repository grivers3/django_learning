from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    # extra_content = {'today': datetime.today()}

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return {'today': datetime.today()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'
