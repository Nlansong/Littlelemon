from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Booking, Menu
from .serializers import bookingSerializer, menuSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    
class BookingViewset(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
    permission_classes=[IsAuthenticated]
    
 
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

@api_view()
@permission_classes([IsAuthenticated])
def secret_message(request):
    return Response("Message is a secret and protected")
    