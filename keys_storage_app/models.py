from django.db import models


class SharedEmail(models.Model):
    email = models.EmailField()
    visited = models.BooleanField()
    info_ip = models.CharField(max_length=200)


class KeyModel(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=10)
    shared_at = models.ForeignKey(SharedEmail, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)
