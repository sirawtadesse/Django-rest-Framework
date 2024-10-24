
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('coach', 'Coach'),
        ('agent', 'Agent'),
        ('football_player', 'Football Player'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='football_player')

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
