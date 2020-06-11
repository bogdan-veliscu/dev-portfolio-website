from django.shortcuts import render

from braces.views import SelectRelatedMixin
from . import models
from django.views import generic
# Create your views here.


class SkillList(generic.ListView):
    model = models.Skill
