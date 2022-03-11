from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import authenticate, login

from django.http import HttpResponseRedirect
from django.views.generic import View

from .forms import *
from .models import *


class BaseView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'base.html', context)


class CVView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'CV.html', context)


class AboutView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'about.html', context)


class FAQsView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'faqs.html', context)


class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {
            'form': form
        }
        return render(request, 'login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(
                username=username,
                password=password
            )
            if user:
                login(request, user)
                return HttpResponseRedirect('/')
        context = {
            'form': form
        }
        return render(request, 'login.html', context)


class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        context = {
            'form': form
        }
        return render(request, 'registration.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Visitor.objects.create(
                user=new_user,
                phone=form.cleaned_data['phone'],
            )
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            login(request, user)
            return HttpResponseRedirect('/')
        context = {
            'form': form
        }
        return render(request, 'registration.html', context)
