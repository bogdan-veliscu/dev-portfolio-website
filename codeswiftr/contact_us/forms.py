from typing import Any, Dict, List, Optional
from django import forms

from django import http
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template import loader
from django.utils.translation import gettext_lazy as _
from .models import ContactEntry

StringKeyedDict = Dict[str, Any]


class ContactForm(forms.Form):
    """
    The base contact form class which all contact form classes should inherit
    """

    name = forms.CharField(max_length=100, label=_("Your name"))
    email = forms.EmailField(label=_("Your email address"))
    user_subject = forms.CharField(max_length=100, label=_("Your subject"))
    body = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 80, 'cols': 20}), label=_("Your message"))

    from_email = settings.DEFAULT_FROM_EMAIL

    recipient_list = [mail_tuple[1] for mail_tuple in settings.MANAGERS]

    subject_template_name = "contact_us/contact_us_subject.txt"
    template_name = "contact_us/contact.html"

    def __init__(
        self,
        data: Optional[StringKeyedDict] = None,
        files: Optional[StringKeyedDict] = None,
        request: Optional[http.HttpRequest] = None,
        recipient_list: Optional[List[str]] = None,
        *args,
        **kwargs
    ):
        if request is None:
            raise TypeError("Keyword argument 'request' must be suplied")
        self.request = request

        if recipient_list is not None:
            self.recipient_list = recipient_list
        super().__init__(data=data, files=files, *args, **kwargs)

    def message(self) -> str:
        """
        Render the body of the message to a string.

        """
        template_name = (self.template_name if callable(
            self.template_name) else self.template_name)

        return loader.render_to_string(
            template_name, self.get_context(), request=self.request
        )

    def subject(self) -> str:
        """
        Render the subject of the message to a string

        """
        template_name = (
            self.subject_template_name()
            if callable(self.subject_template_name)
            else self.subject_template_name
        )
        subject = loader.render_to_string(
            template_name, self.get_context(), request=self.request
        )
        return "".join(subject.splitlines())

    def get_context(self) -> StringKeyedDict:
        """
        Return the context used to render the template for the email subject and body

        By default, this context includes:
        * All of the validated values in the form, as variables of the
          same names as their fields.
        * The current ``Site`` object, as the variable ``site``.
        * Any additional variables added by context processors (this
          will be a ``RequestContext``).

        """
        if not self.is_valid():
            raise ValueError(
                "Cannot generate Context from invalid contact form")
        return dict(self.cleaned_data, site=get_current_site(self.request))

    def get_message_dict(self) -> StringKeyedDict:
        """
        Generate the various parts of the message and return them in a
        dictionary, suitable for passing directly as keyword arguments
        to ``django.core.mail.send_mail()``.
        By default, the following values are returned:
        * ``from_email``
        * ``message``
        * ``recipient_list``
        * ``subject``
        """
        if not self.is_valid():
            raise ValueError(
                "Message cannot be sent from invalid contact form")
        message_dict = {}
        for message_part in ("from_email", "message", "recipient_list", "subject"):
            attr = getattr(self, message_part)
            message_dict[message_part] = attr() if callable(attr) else attr
        return message_dict

    def save(self, fail_silently: bool = False) -> None:
        """
        Build and send the email message.
        """
        context = self.get_context()
        print("\n# Contact FORM :\n\n", context)

        message_entry = ContactEntry(
            name=context['name'], subject=context['user_subject'], email=context['email'], message=context['body'])
        message_entry.save()
        send_mail(fail_silently=fail_silently, **self.get_message_dict())
