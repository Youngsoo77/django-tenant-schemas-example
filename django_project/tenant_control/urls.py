# Third Party
from django.urls import path

# Project
from .views import CompanyList, CreateCompany, UpdateCompany


urlpatterns = [
    path('', CompanyList.as_view(), name='company-list'),
    path('tenant/', CreateCompany.as_view(), name='company-create'),
    path('tenant/<int:pk>/', UpdateCompany.as_view(), name='company-update'),
]
