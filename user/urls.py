from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user_view, name='example'),
    path('user/create/', views.create_user, name='create_user'),
    path('user/<int:user_id>', views.get_user, name='get_user'),
]