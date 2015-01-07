from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from categories.models import *
from institutions.models import Institution, Area
from listings.models import *


def categories(request, abbr=None, section_slug=None, template='categories/categories_list.html'):
    institution = get_object_or_404(Institution, abbr=abbr)
    areas = Area.objects.filter(institution=institution)
    categories = ''
    section = ''
    listings = ''
    if section_slug == 'for-sale':
        section = "For Sale"
        categories = SaleCategory.objects.all()
        listings = Sale.objects.filter(category=categories, area=areas, active=True)
    elif section_slug == 'community':
        section = "Community"
        categories = CommunityCategory.objects.all()
        listings = Community.objects.filter(category=categories, area=areas, active=True)
    elif section_slug == 'housing':
        section = "Housing"
        categories = HousingCategory.objects.all()
        listings = Housing.objects.filter(category=categories, area=areas, active=True)
    elif section_slug == 'events':
        section = "Events"
        categories = EventCategory.objects.all()
        listings = Event.objects.filter(category=categories, area=areas, active=True)
    elif section_slug == 'services':
        section = "Services"
        categories = ServiceCategory.objects.all()
        listings = Service.objects.filter(category=categories, area=areas, active=True)
    elif section_slug == 'discussions':
        return redirect('/%s/discussions' %(institution.abbr))
    else:
        raise Http404
    return render(request, template, {'categories':categories, 'institution':institution, 'section':section,
                                      'section_slug':section_slug, 'listings':listings})