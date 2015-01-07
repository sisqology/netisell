from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from institutions.models import Institution, Area
from listings.models import Sale


def sections(request, abbr=None, template="sections/sections_list.html"):
    institution = get_object_or_404(Institution, abbr=abbr)
    areas = Area.objects.filter(institution=institution)
    return render(request, template, {'institution':institution, 'areas':areas})