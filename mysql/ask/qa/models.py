from django.db import models
from django.contrib.auth.models import User
class Question(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField()
    author = models.OneToOneField(User)
    likes = models.IntegerField()
    class Meta:
        ordering = ['-rating']

class QuestionManager():
    def new():
        import datetime
        today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
        today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        return Question.objects.get(added_at__range=(today_min, today_max))

    def popular():
        return Question.objects

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question)
    author = models.OneToOneField(User)    