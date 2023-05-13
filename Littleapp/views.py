from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Booking, Menu
from .serializers import bookingSerializer, menuSerializer
from rest_framework import generics

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    
class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
 
# class BookingView(APIView):
#     def get(self, request):
#         items = Booking.objects.all()
#         serializer = bookingSerializer(items, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = menuSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status':'success', 'data':'serializer.data'})

def index(request):
    return render(request, 'index.html', {})