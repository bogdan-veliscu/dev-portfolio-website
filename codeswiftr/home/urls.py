from . import views
from django.urls import path, include
app_name = 'home'

urlpatterns = [
    path('', views.homepage, name='home'),
    path('contact', include('contact_us.urls')),
]
