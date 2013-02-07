from django.db import models
from django.db.models.signals import post_save
# Create your models here.
import requests

class Record(models.Model):
    sender = models.CharField(max_length=50)
    message = models.SlugField(max_length=50, unique=True, help_text='Unique value for product page URL, created from name.')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'store'
        ordering = ['-created_at']
        verbose_name_plural = 'Records'
    def __unicode__(self):
        return self.sender

def notify(sender, **kwargs):
    params = {}
    params['to'] = kwargs['instance'].sender
    params['text'] = 'This is the reply'
    params['username'] = 'kanneluser'
    params['password'] = 'df89asj89I23hvcxSDasdf3298jvkjc839'
    requests.get('http://localhost:13777/cgi-bin/sendsms', params=params)

post_save.connect(notify, sender=Record, dispatch_uid="test_app.models")
