from django.urls import path

from .views import *

urlpatterns = [
    path('', BaseView.as_view(), name='home'),
    path('CV_page/', CVView.as_view(), name='CV page'),
    path('about/', AboutView.as_view(), name='about'),
    path('FAQs/', FAQsView.as_view(), name='faqs'),
    path('sign-up', RegistrationView.as_view(), name='sign-up'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('profile', ProfileView.as_view(), name='profile'),
]
