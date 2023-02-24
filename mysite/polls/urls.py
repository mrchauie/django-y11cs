from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.QuestionView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.VoteView.as_view(), name='vote'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    # # path("register", views.register_request, name="register"),
    path("register", views.RegisterUserFormView.as_view(), name="register"),
    ]