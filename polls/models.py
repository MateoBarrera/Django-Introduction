import datetime
from secrets import choice
from statistics import mode
from django.db import models
from django.utils import timezone

#Modelo ORM para las preguntas
class Question(models.Model):
  #El campo ID es autoincremental e implícito en Django
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

  def __str__(self):
    return self.question_text

  def was_published_recently(self):
    return timezone.now() >= self.pub_date >= timezone.now()-datetime.timedelta(days=1)

class Choice(models.Model):
  #Llave foranea asociada a los campos de Question, on_delete..CASCADE eliminara las choices asociadas en caso de eliminar la question asociada
  question  = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

  def __str__(self):
    return self.choice_text
