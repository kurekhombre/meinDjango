from django.urls import path 
from intro import views

urlpatterns = [
    path('card/', views.buisness_card)
]
