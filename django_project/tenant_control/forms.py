# Third Party
from django.contrib.auth.forms import UsernameField
from django import forms

# Project
from .models import Company


class CreateCompanyForm(forms.ModelForm):
    username = UsernameField(max_length=254)
    email = forms.EmailField(label='Email', max_length=254)
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput,
    )

    def __init__(self, *args, **kwargs):
        super(CreateCompanyForm, self).__init__(*args, **kwargs)

        self.fields['domain_url'].widget.attrs['placeholder'] = '{{ subdomain }}.localhost'

    class Meta:
        model = Company
        fields = ['name', 'domain_url', 'schema_name', 'username', 'email', 'password']


class UpdateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'domain_url']
