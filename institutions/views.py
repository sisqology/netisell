from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from institutions.models import Institution


class InstitutionList(ListView):
    queryset = Institution.objects.all()
    template_name = "institutions/institutions_list.html"
    context_object_name = "institutions"
    #response_object_name = "templates"

    def get_context_data(self, **kwargs):
        context = super(InstitutionList, self).get_context_data(**kwargs)
        context['institutions'] = Institution.objects.all().order_by("abbr")
        #TODO: cookies/sessions for institutions
        return context