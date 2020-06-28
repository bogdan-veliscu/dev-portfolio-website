from django.urls import path
from django.views.generic import TemplateView
from .views import ContactFormView

urlpatterns = [
    path("", ContactFormView.as_view(), name="contact_us"),
    path(
        "sent/",
        TemplateView.as_view(
            template_name="home/landing.html"),
        name="contact_form_sent",
    ),
]
