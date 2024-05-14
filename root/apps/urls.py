from django.urls import path
from .views import Home, UserDeleteView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('delete/<int:pk>', UserDeleteView.as_view(), name='delete'),
]
