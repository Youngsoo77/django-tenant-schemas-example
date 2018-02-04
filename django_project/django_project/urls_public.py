# Third Party
from django.urls import include, path


urlpatterns = [
    path('', include('tenant_control.urls')),
]
