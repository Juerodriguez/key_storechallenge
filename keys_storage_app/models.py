from django.db import models
from django.core import validators


class SharedEmail(models.Model):
    email = models.EmailField(validators=[validators.validate_email])
    visited = models.BooleanField(default=False)
    info_ip = models.CharField(max_length=100, blank=True, null=True)


class KeyModel(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    shared_at = models.ForeignKey(SharedEmail, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)
