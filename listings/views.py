from django.forms import Form
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from categories.models import *
from institutions.models import Institution, Area
from listings.forms import *
from listings.models import *


def add(request, template='listings/add.html'):
    listing_form = Form
    category_form = CategoryForm(request.POST)
    context = {}
    selected_category = ''
    context['category_form'] = category_form
    if 'select_category' in request.POST and request.method == 'POST':
        selected_category = request.POST.get('category')
        if selected_category == 'for-sale':
            listing_form = SaleForm(request.POST, request.FILES, prefix='sale')
            context['listing_form'] = listing_form
            context['option'] = selected_category
        elif selected_category == 'event':
            listing_form = EventForm(request.POST, request.FILES, prefix='event')
            context['listing_form'] = listing_form
            context['option'] = selected_category
        elif selected_category == 'service':
            listing_form = ServiceForm(request.POST, request.FILES, prefix='service')
            context['listing_form'] = listing_form
            context['option'] = selected_category
        elif selected_category == 'housing':
            listing_form = HousingForm(request.POST, request.FILES, prefix='housing')
            context['listing_form'] = listing_form
            context['option'] = selected_category
        elif selected_category == 'community':
            listing_form = HousingForm(request.POST, prefix='community')
            context['listing_form'] = listing_form
            context['option'] = selected_category
    if 'post_ad' in request.POST and request.method == 'POST' and request.POST.get('option') == 'for-sale':
        listing_form = SaleForm(request.POST, request.FILES, prefix='sale')
        if listing_form.is_valid():
            listing_form.save()
        else:
            context['listing_form'] = listing_form
            context['option'] = 'for-sale'
    if 'post_ad' in request.POST and request.method == 'POST' and request.POST.get('option') == 'event':
        listing_form = EventForm(request.POST, request.FILES, prefix='event')
        if listing_form.is_valid():
            listing_form.save()
        else:
            context['listing_form'] = listing_form
            context['option'] = 'event'
    if 'post_ad' in request.POST and request.method == 'POST' and request.POST.get('option') == 'service':
        listing_form = ServiceForm(request.POST, request.FILES, prefix='service')
        if listing_form.is_valid():
            listing_form.save()
        else:
            context['listing_form'] = listing_form
            context['option'] = 'service'
    if 'post_ad' in request.POST and request.method == 'POST' and request.POST.get('option') == 'housing':
        listing_form = HousingForm(request.POST, request.FILES, prefix='housing')
        if listing_form.is_valid():
            listing_form.save()
        else:
            context['listing_form'] = listing_form
            context['option'] = 'housing'
    if 'post_ad' in request.POST and request.method == 'POST' and request.POST.get('option') == 'community':
        listing_form = CommunityForm(request.POST, prefix='community')
        if listing_form.is_valid():
            listing_form.save()
        else:
            context['listing_form'] = listing_form
            context['option'] = 'community'
    return render(request, template, context)

def listings(request, abbr=None, section_slug=None, category_slug=None, template='listings/listings_index.html'):
    category = ''
    listings = ''
    institution = get_object_or_404(Institution, abbr=abbr)
    areas = Area.objects.filter(institution=institution)
    if section_slug == 'for-sale':
        section = "For Sale"
        category = get_object_or_404(SaleCategory, slug=category_slug)
        listings = Sale.objects.filter(category=category, area=areas, active=True)
    elif section_slug == 'community':
        section = "Community"
        category = get_object_or_404(CommunityCategory, slug=category_slug)
        listings = Community.objects.filter(category=category, area=areas, active=True)
    elif section_slug == 'housing':
        section = "Housing"
        category = get_object_or_404(HousingCategory, slug=category_slug)
        listings = Housing.objects.filter(category=category, area=areas, active=True)
    elif section_slug == 'events':
        section = "Events"
        category = get_object_or_404(EventCategory, slug=category_slug)
        listings = Event.objects.filter(category=category, area=areas, active=True)
    elif section_slug == 'services':
        section = "Services"
        category = get_object_or_404(ServiceCategory, slug=category_slug)
        listings = Service.objects.filter(category=category, area=areas, active=True)
    elif section_slug == 'discussions':
        return redirect('/%s/discussions' %(institution))
        #section = "Discussions"
        #category = get_object_or_404(DiscussionCategory, slug=category_slug)
        #listings = Discussion.objects.filter(category=category, area=areas, active=True)
    else:
        raise Http404
    return render(request, template, {'category':category, 'institution':institution, 'listings':listings, 'section':section,
                                      'section_slug':section_slug})

def post(request, abbr=None, section_slug=None, post_id=None, post_slug=None, template='listings/view_listing.html'):
    institution = Institution.objects.get(abbr=abbr)
    listing_render = ''
    if section_slug == 'for-sale':
        listing_render = get_object_or_404(Sale, id=post_id, slug=post_slug)
    elif section_slug == 'community':
        listing_render = get_object_or_404(Community, id=post_id, slug=post_slug)
    elif section_slug == 'housing':
        listing_render = get_object_or_404(Housing, id=post_id, slug=post_slug)
    elif section_slug == 'events':
        listing_render = get_object_or_404(Event, id=post_id, slug=post_slug)
    elif section_slug == 'services':
        listing_render = get_object_or_404(Service, id=post_id, slug=post_slug)
    #listing_render = Listing.objects.get(institution=institution, id=listing_id, slug=listing_slug)
    return render(request, template, {'listing':listing_render})