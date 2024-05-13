from django.urls import path
from .views import Home, DeletePeople

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('delete/<int:pk>', DeletePeople.as_view(), name='delete'),
]
