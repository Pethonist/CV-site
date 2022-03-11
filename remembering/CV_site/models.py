from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Visitor(models.Model):
    id = models.PositiveIntegerField(default=0, unique=True, primary_key=True, verbose_name='id num of user')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    first_name = models.CharField(max_length=255, verbose_name='Name of user')
    last_name = models.CharField(max_length=255, verbose_name='Surname of user')
    email_address = models.CharField(max_length=255, unique=True, verbose_name='Email address of user')
    phone = models.CharField(max_length=25, )

    def __str__(self):
        return 'User: {} {}'.format(self.first_name, self.last_name)


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Sender of message')
    text = models.TextField(null=True, verbose_name='Text of message')

    def __str__(self):
        return self.text
