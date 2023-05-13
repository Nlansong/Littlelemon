from django.urls import path
from .views import BookingView, index, MenuItemView, SingleMenuItemView

urlpatterns  = [
    path('index/', index, name='index'),
    path('booking/', BookingView.as_view()),
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
]