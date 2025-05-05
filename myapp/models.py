from django.db import models

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class QuoteRequest(models.Model):
    SERVICE_CHOICES = [
        ('Security Guards', 'Security Guards'),
        ('Security Supervisor', 'Security Supervisor'),
        ('GunMan', 'GunMan'),
        ('Housekeeping', 'Housekeeping'),
        ('Pantry Boy', 'Pantry Boy'),
        ('Gardner', 'Gardner'),
        ('Fire Safety Service', 'Fire Safety Service'),
        ('Other Services', 'Other Services'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service}"