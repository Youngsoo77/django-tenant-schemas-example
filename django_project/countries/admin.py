# Third Party
from django.db import connection
from django.contrib import admin
from tenant_schemas.utils import get_public_schema_name

# Project
from .models import Country


class CountryAdmin(admin.ModelAdmin):
    """Countries must be readonly on non-public schemas."""

    list_display = ['code', 'name']

    def _is_public_schema(self):
        return connection.schema_name == get_public_schema_name()

    def get_actions(self, *args, **kwargs):
        if not self._is_public_schema():
            return None
        return super(CountryAdmin, self).get_actions(*args, **kwargs)

    def get_readonly_fields(self, *args, **kwargs):
        if not self._is_public_schema():
            return [f.name for f in Country._meta.get_fields()]
        return super(CountryAdmin, self).get_readonly_fields(*args, **kwargs)

    def has_add_permission(self, *args, **kwargs):
        if not self._is_public_schema():
            return False
        return super(CountryAdmin, self).has_add_permission(*args, **kwargs)

    def has_delete_permission(self, *args, **kwargs):
        if not self._is_public_schema():
            return False
        return super(CountryAdmin, self).has_delete_permission(*args, **kwargs)

    def log_change(self, *args, **kwargs):
        if not self._is_public_schema():
            return False
        return super(CountryAdmin, self).log_change(*args, **kwargs)

    def message_user(self, *args, **kwargs):
        if not self._is_public_schema():
            return False
        return super(CountryAdmin, self).message_user(*args, **kwargs)

    def save_model(self, *args, **kwargs):
        if not self._is_public_schema():
            return False
        return super(CountryAdmin, self).save_model(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        if not self._is_public_schema():
            extra_context = kwargs.get('extra_context', {})
            extra_context['show_save_and_continue'] = False
            extra_context['show_save'] = False
            kwargs['extra_context'] = extra_context
        return super(CountryAdmin, self).change_view(*args, **kwargs)


admin.site.register(Country, CountryAdmin)
