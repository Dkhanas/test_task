from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from companies.models import MainCompany, SubsidiaryCompany


def main(request):
    main_companies = get_list_or_404(MainCompany)
    return render(request, 'base.html', {'main_companies': main_companies})


def main_company(request, main_id):
    get_main = get_object_or_404(MainCompany, pk=main_id)
    subsidiaries = SubsidiaryCompany.objects.filter(main_company=get_main)
    return render(request, 'main_company.html',
                  {'get_main': get_main, 'subsidiaries': subsidiaries})


class SubsidiaryCompanyCreate(CreateView):
    template_name = 'create_form.html'
    model = SubsidiaryCompany
    fields = ['name', 'annual_earning', 'main_company', 'parent']
    success_url = reverse_lazy('main')


class SubsidiaryCompanyUpdate(UpdateView):
    template_name = 'edit_form.html'
    model = SubsidiaryCompany
    fields = ['name', 'annual_earning', 'main_company', 'parent']
    success_url = reverse_lazy('main')


class SubsidiaryCompanyDelete(DeleteView):
    template_name = 'company_confirm_delete.html'
    model = SubsidiaryCompany
    success_url = reverse_lazy('main')
