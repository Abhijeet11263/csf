from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .forms import QuoteForm


from .forms import ContactForm

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def project(request):
    return render(request, 'project.html')

def feature(request):
    return render(request, 'feature.html')

def quote(request):
    return render(request, 'quote.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Thank you for contacting us! We will get back to you soon.'})
        else:
            return JsonResponse({'success': False, 'message': 'Please fill all required fields correctly.'}, status=400)
    
    return render(request, 'contact.html')


def submit_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'success': True,
                'message': 'Thank you for your request! We will contact you shortly with a quote.'
            })
        else:
            return JsonResponse({
                'success': False,
                'message': 'Please fill all required fields correctly.'
            }, status=400)
    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)