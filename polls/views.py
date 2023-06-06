from django.shortcuts import render

from .models import Question

from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá Mundo! Esta é a página inicial do aplicativo.")

# Create your views here.

def sobre(request):
    return HttpResponse("Esta é a página sobre do meu site")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)




def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


# Leave the rest of the views (detail, results, vote) unchanged
