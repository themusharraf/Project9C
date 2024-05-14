from django.views.generic import ListView, DeleteView
from .models import People


class Home(ListView):
    model = People
    context_object_name = 'users'
    template_name = 'User_list.html'


class UserDeleteView(DeleteView):
    model = People
    pk_url_kwarg = "pk"
    success_url = "/"
    template_name = 'User_list.html'

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


