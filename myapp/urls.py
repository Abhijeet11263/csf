from django.urls import path
from . import views
from .views import contact, submit_quote



urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('project/', views.project, name='project'),
    path('feature/', views.feature, name='feature'),
    path('quote/', views.quote, name='quote'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('contact/', contact, name='contact'),
    path('submit-quote/', submit_quote, name='submit_quote'),
]
