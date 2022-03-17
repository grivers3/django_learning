from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import redirect

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    # extra_content = {'today': datetime.today()}

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return {'today': datetime.today()}

# * No Longer Needed
# class AuthorizedView(LoginRequiredMixin, TemplateView):
    # template_name = 'home/authorized.html'
    # login_url = '/admin'
