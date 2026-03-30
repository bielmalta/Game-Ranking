from django.urls import path
from . import views

urlpatterns = [
    path('rate/<int:pk>/', views.rate_game, name='rate_game'),
    path('comment/<int:pk>/', views.save_comment, name='save_comment'),
]