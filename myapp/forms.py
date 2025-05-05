from django import forms
from .models import ContactSubmission
from .models import QuoteRequest


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'subject', 'message']


class QuoteForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ['name', 'email', 'mobile', 'service', 'notes']
