from django import forms
from django.core.mail import send_mail
from django.conf import settings

from core.mail import send_mail_template

class Contact(forms.Form):
    email = forms.EmailField(label='E-mail')

    def __init__(self, *args, **kwargs):
        super(Contact, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'

    def send_mail(self):
        subject = 'Contato'
        context = {
            'email': self.cleaned_data['email'],
        }
        template_name = 'contact_email.html'
        send_mail_template(subject, template_name, context, [settings.CONTACT_EMAIL])
