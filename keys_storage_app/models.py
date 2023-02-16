from django.db import models
from django.core import validators


class KeyModel(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)


class SharedEmail(models.Model):
    email = models.EmailField(validators=[validators.validate_email])
    visited = models.BooleanField(default=False)
    info_ip = models.CharField(max_length=100, blank=True, null=True)
    key_related = models.ForeignKey(KeyModel, related_name='shared_at',
                                    on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.email
