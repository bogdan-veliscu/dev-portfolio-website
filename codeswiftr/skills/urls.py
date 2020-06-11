from django.urls import path

from . import views
app_name = 'skill'
urlpatterns = [
    path('', views.SkillList.as_view(), name='all'),
]
