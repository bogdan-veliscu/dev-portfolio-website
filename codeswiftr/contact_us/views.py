from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django import http
from .forms import ContactForm, StringKeyedDict
# Create your views here.


class ContactFormView(FormView):
    form_class = ContactForm
    recipient_list = None
    success_url = "contact_us/contact.html"

    template_name = 'contact_us/contact.html'

    def form_valid(self, form) -> http.HttpResponse:
        print("# form_valid")
        form.save()
        return super().form_valid(form)

    def get_form_kwargs(self) -> StringKeyedDict:
        kwargs = super().get_form_kwargs()
        kwargs.update({"request": self.request})

        if self.recipient_list is not None:
            kwargs.update({"recipient_list": self.recipient_list})
        return kwargs
