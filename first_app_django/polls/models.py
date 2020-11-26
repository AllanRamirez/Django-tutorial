import datetime

from django.db import models
from django.utils import timezone

#cada class es un modelo
#claves primarias (id's) se crean automaticamente, esto se puede anular

# basicamente creamos una tabla polls.question (nombre del app + nombre del modelo) con 2 columnas, question_text y pub_date
class Question(models.Model):
    question_text = models.CharField(max_length=200) 
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# basicamente creamos una tabla polls.choice (nombre del app + nombre del modelo) con 2 columnas, question, choice_text y vores
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #al hacer esto puedo hacer querysets con una relacion a la foreign key. q.choice_set.create(choice_text='Not much', votes=0) where q is q = Question.objects.get(pk=1)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
'''
Guía de tres pasos para hacer cambios de modelo:

Cambie sus modelos (en models.py).
Ejecute el comando python manage.py makemigrations para crear migraciones para esos cambios
Ejecute el comando python manage.py migrate para aplicar esos cambios a la base de datos.
'''


