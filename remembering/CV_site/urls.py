from django.urls import path

from .views import *

urlpatterns = [
    path('', BaseView.as_view(), name='home'),
    path('CV_page', CVView.as_view(), name='CV page'),
    path('about', AboutView.as_view(), name='about'),
]
