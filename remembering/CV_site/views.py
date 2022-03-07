from django.shortcuts import render
from django.shortcuts import redirect

from django.views.generic import View


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


