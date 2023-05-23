from django.db import models

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
# Create your models here.


class Usuario(models.Model):
nome = models.CharField(max_length=50)
nickname = models.CharField(max_length=100, unique=True)
avatar = models.CharField(max_length=255, null=True)

def __str__(self):
return self.nome


class Questionario(models.Model):
titulo = models.CharField(max_length=100)
descricao = models.CharField(max_length=500, null=True)
data_criacao = models.DateTimeField(auto_now_add=True)
capa = models.CharField(max_length=255, null=True)
usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

def __str__(self):
return self.titulo


class Hashtag(models.Model):
tag = models.CharField(max_length=100, unique=True)

def __str__(self):
return self.tag


class HashtagHasQuestionario(models.Model):
hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE)
questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE)

def __str__(self):
return f"{self.hashtag} - {self.questionario}"
