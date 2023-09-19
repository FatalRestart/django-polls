from django.urls import path

from . import views

urlpatterns = [
    # # ex: /polls/
    # path("", views.index, name="index"),

    # # ex: /polls/5/
    # path("<int:question_id>/", views.detail, name="detail"),

    # # ex: /polls/5/results/
    # path("<int:question_id>/resultados/", views.results, name="results"),
    
    # # ex: /polls/5/vote/
    # path("<int:question_id>/votar/", views.vote, name="vote"),

    # página de cadastro de nova enquete
    path('listar', views.QuestionListView.as_view(), name="question-list"),
    path('cadastrar', views.QuestionCreateView.as_view(), name="question-create"),
    path('<int:pk>', views.QuestionDetailView.as_view(), name='question-detail'),
    path('<int:pk>/deletar', views.QuestionDeleteView.as_view(), name='question-delete'),
    path('<int:pk>/atuaizar', views.QuestionUpdateView.as_view(), name='question-update')
]
