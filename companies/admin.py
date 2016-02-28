from django.contrib import admin

from companies.models import MainCompany, SubsidiaryCompany

admin.site.register(MainCompany)
admin.site.register(SubsidiaryCompany)