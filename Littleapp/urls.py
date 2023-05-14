from django.urls import path
from .views import index, MenuItemView, SingleMenuItemView, secret_message
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns  = [
    path('index/', index, name='index'),
    # path('booking/', BookingView.as_view()),
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('message/', secret_message),
    path('api-auth-token', obtain_auth_token),
]