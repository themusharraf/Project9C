from django.views.generic import ListView
from .models import People


class Home(ListView):
    model = People
    context_object_name = 'users'
    template_name = 'User_list.html'
