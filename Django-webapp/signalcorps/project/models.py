from django.db import models
from django.utils.translation import gettext as _
import datetime


class SignalCorps(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    rank = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Communication(models.Model):
    c_id = models.IntegerField(primary_key=True)
    s_id = models.ForeignKey(SignalCorps, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateField(_("Date"), auto_now_add=True)

    
