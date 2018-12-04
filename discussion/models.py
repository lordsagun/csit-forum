from django.db import models
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField
# from discussion.settings import AUTH_USER_MODEL
from forum import settings

# Create your models here.

class Questions(models.Model):
    asked_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    question_body = models.CharField(max_length=1000)
    image = models.FileField(upload_to='question')
    semester = models.IntegerField()
    subject = models.CharField(max_length=100)
    number_of_ans = models.IntegerField()
    number_of_views = models.IntegerField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL,default=1)

    def __str__(self):
        return self.question_body

class Answers(models.Model):
    answer_at = models.DateTimeField()
    answer_body = models.CharField(max_length=1000)
    upvote = models.IntegerField()
    downvote = models.IntegerField()
    question = models.ForeignKey(Questions)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,default=1)

    def __str__(self):
        return self.answer_body

class Answer_reply(models.Model):
    pass
    answer_reply_at = models.DateTimeField()
    answer_reply_body = models.CharField(max_length=100)
    upvote = models.IntegerField()
    downvote = models.IntegerField()
    question = models.ForeignKey(Questions)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,default=1)

    def __str__(self):
        return self.answer_reply_body
