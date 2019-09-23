import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

# class Post(models.Model):
#     content = models.CharField(max_length=2000)
#     pub_date = models.DateTimeField('date published')
#     user_id = models.ForeignKey('User', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.content
    
#     def was_published_recently(self):
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= self.pub_date <= now
#     was_published_recently.admin_order_field = 'pub_date'
#     was_published_recently.boolean = True
#     was_published_recently.short_description = 'Published recently?'
