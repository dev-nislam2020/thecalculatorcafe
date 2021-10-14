from django.urls import path
from .views import index, list, detail, contact, about, privicy

urlpatterns = [
    path('', index, name='index'),
    path('list/', list, name='calculator_list'),
    path('detail/<slug:slug>/', detail, name='calculator_detail'),
    path('contact/', contact, name='calculator_contact'),
    path('about/', about, name='calculator_about'),
    path('privicy', privicy, name='calculator_privicy'),
]