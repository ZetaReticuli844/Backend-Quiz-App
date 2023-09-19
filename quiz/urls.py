from django.urls import path
from . import views
urlpatterns = [
    path('quiz/', views.quiz_list, name='quiz_list'),
    path('quiz/create/', views.quiz_create, name='quiz_create'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/<int:quiz_id>/question/create/', views.question_create, name='question_create'),
    path('question/<int:question_id>/choice/create/', views.choice_create, name='choice_create'),
    path('user_response/create/', views.user_response_create, name='user_response_create'),
    path('quiz/<int:quiz_id>/user_response/list/', views.user_response_list, name='user_response_list'),
    
]
