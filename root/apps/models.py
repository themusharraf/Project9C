from django.db import models


class People(models.Model):
    full_name = models.CharField(max_length=225)
    is_staff = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=225)
    email = models.CharField(max_length=225)

    def __str__(self):
        return self.full_name
