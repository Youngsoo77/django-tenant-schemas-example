# Third Party
from django.contrib.auth import get_user_model
from django.db import connection
from django.contrib import admin
from tenant_schemas.utils import get_public_schema_name, schema_context

# Project
from .forms import CreateCompanyForm, UpdateCompanyForm
from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    """Companies must be unavailable on non-public schemas."""

    list_display = ['name', 'domain_url', 'schema_name']
    list_display_links = list_display

    def _is_public_schema(self):
        return connection.schema_name == get_public_schema_name()

    def has_module_permission(self, *args, **kwargs):
        if not self._is_public_schema():
            return False
        return super(CompanyAdmin, self).has_module_permission(*args, **kwargs)

    def get_form(self, request, obj=None, **kwargs):
        if obj and obj.pk:
            kwargs['form'] = UpdateCompanyForm
        else:
            kwargs['form'] = CreateCompanyForm
        return super(CompanyAdmin, self).get_form(request, obj, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super(CompanyAdmin, self).get_readonly_fields(request, obj)
        if obj and obj.pk and ('schema_name' not in readonly_fields):
            readonly_fields = list(readonly_fields)
            readonly_fields.append('schema_name')
        return readonly_fields

    def save_model(self, request, obj, form, change):
        super(CompanyAdmin, self).save_model(request, obj, form, change)
        if not change:
            # Just created the Company and its schema. Now create a superuser for it.
            UserModel = get_user_model()
            data = form.cleaned_data
            with schema_context(data['schema_name']):
                UserModel.objects.create_superuser(
                    username=data['username'],
                    email=data['email'],
                    password=data['password']
                )


admin.site.register(Company, CompanyAdmin)
