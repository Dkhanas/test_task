from django.conf.urls import url

from companies import views
from companies.views import SubsidiaryCompanyCreate, SubsidiaryCompanyUpdate, \
    SubsidiaryCompanyDelete

urlpatterns = [
    url(r'^(?P<main_id>\d+)$', views.main_company,
        name='main_company'),
    url(r'^add$', SubsidiaryCompanyCreate.as_view(), name='add'),
    url(r'^(?P<pk>\d+)/edit$', SubsidiaryCompanyUpdate.as_view(),
        name='edit'),
    url(r'^(?P<pk>\d+)/delete$', SubsidiaryCompanyDelete.as_view(),
        name='delete')
]
