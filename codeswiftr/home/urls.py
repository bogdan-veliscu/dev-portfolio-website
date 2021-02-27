from . import views
from django.urls import path, include
app_name = 'home'

urlpatterns = [
    path('', views.homepage, name='home'),
    #path('demo', views.demo, name='demo'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    # path('contact', include('contact_us.urls')),
]
