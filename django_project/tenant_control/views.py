# Third Party
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy
from tenant_schemas.utils import schema_context

# Project
from .forms import CreateCompanyForm, UpdateCompanyForm
from .models import Company


class CompanyList(ListView):
    model = Company


class CreateCompany(CreateView):
    model = Company
    form_class = CreateCompanyForm
    success_url = reverse_lazy('company-list')

    def form_valid(self, form):
        redirect = super(CreateCompany, self).form_valid(form)

        # Create a superuser in the newly created schema with the login data from the form
        UserModel = get_user_model()
        data = form.cleaned_data
        with schema_context(data['schema_name']):
            UserModel.objects.create_superuser(
                username=data['username'],
                email=data['email'],
                password=data['password']
            )

        return redirect


class UpdateCompany(UpdateView):
    model = Company
    form_class = UpdateCompanyForm
    success_url = reverse_lazy('company-list')
