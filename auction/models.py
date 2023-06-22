import os, datetime
from django.db import models
from django.conf import settings
#from users.models import CustomUser

class Item(models.Model): 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=600, default='', blank=True)
    item_image = models.ImageField(upload_to='auction/frontend/public/', default="")
    end_date = models.DateField(default=datetime.date.today)
    end_time = models.TimeField(default=datetime.time.max)

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user,
            'title': self.title,
            'starting_price': self.starting_price,
            'description': self.description,
            'item_image': self.item_image.url,
            'end_date': self.end_date,
            'end_time': self.end_time
        }
    
    def get_image(self):
        if self.item_image:
            return 'http://localhost:8000' + self.item_image
        return ''

class Bid(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='bids', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='bids', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        string = str(self.amount)
        return string
    
    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user,
            'item': self.item,
            'amount': self.amount
        }

class Question(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='questions', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='questions', on_delete=models.CASCADE, null=True)
    question = models.TextField(max_length=600, default='', blank=True)

    def __str__(self):
        return self.question

    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user,
            'item': self.item,
            'queston': self.question,
        }

class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='answers', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='answers', on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE, null=True)
    answer = models.TextField(max_length=600, default='', blank=True)

    def __str__(self):
        return self.answer

    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user,
            'item': self.item,
            'question': self.question,
            'answer': self.answer,
        }