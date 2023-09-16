from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_view, name='example'),
    path('create/', views.create_user, name='create_user'),
    path('<int:user_id>', views.get_user, name='get_user'),
]