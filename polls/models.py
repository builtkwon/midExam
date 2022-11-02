import datetime
from django.utils import timezone
from django.db import models

# Create your models here.
class Question(models.Model):
    object={}#views.py에서 발생한 경고 해결 위해 형식상 삽입한 문법
             # Unresolved attribute reference 'objects' for class 'Question'
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)

    was_published_recently.admin_order_field='pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text