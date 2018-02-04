# Third Party
from django.contrib import admin
from django.db import connection
from tenant_schemas.utils import get_public_schema_name

# Project
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    """Customers must be unavailable on the public schema."""

    def _is_public_schema(self):
        return connection.schema_name == get_public_schema_name()

    def has_module_permission(self, *args, **kwargs):
        if self._is_public_schema():
            return False
        return super(CustomerAdmin, self).has_module_permission(*args, **kwargs)


admin.site.register(Customer, CustomerAdmin)
