from . import views
from django.urls import path
app_name = 'projects'


app_name = 'skill'
urlpatterns = [
    path('', views.homepage, name='home'),
]
