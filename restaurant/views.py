from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})
        
class BookingViewSet(viewsets.ModelViewSet):
    queryset  = Booking.objects.all()
    serializer_class = BookingSerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer