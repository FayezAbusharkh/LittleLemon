#define URL route for index() view
from django.urls import path
from . import views
from .views import index, MenuView, BookingView  

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', MenuView.as_view()),
    path('booking/', BookingView.as_view()),
]

