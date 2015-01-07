from django import forms
from listings.models import Sale, Event, Service, Housing, Community


CHOICES = [('for-sale', 'For Sale'),
           ('housing', 'Housing'),
           ('community', 'Community'),
           ('service', 'Services'),
           ('event', 'Events'),
           ]

class CategoryForm(forms.Form):
    category = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    #def __init__(self, *args, **kwargs):
    #    super(CategoryForm, self).__init__(*args, **kwargs)
    #    self.fields['category'].error_messages = {'required': ''}
    #    self.fields['category'].help_text = "Please choose a category"

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['title', 'price', 'negotiable', 'condition', 'phone', 'email', 'area', 'category', 'description',
                  'image1', 'image2', 'image3', 'image4']
        widgets = {
            'title':forms.TextInput(attrs={'placeholder': 'ad title e.g: HP Laptop 630 for sale'}),
            'price':forms.TextInput(attrs={'placeholder': 'item price in figures e.g: 2000, 0 if free'}),
            'phone':forms.TextInput(attrs={'placeholder': 'seller\'s phone number (buyers can contact)'}),
            'email':forms.TextInput(attrs={'placeholder': 'seller\'s email (buyers can contact)'}),
            'description': forms.Textarea(attrs={'placeholder':'ad description, a good and straight description attracts more interest', 'rows':'4'}),
        }

    def save(self, commit=True):
        sale = super(SaleForm, self).save(commit=False)
        sale.active = True
        if sale.price == '':
            sale.price = 0.0
        if commit:
            sale.save()
        return sale


class EventForm(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
    #    super(EventForm, self).__init__(*args, **kwargs)
    #    self.fields['title'].help_text = "Title here"

    class Meta:
        model = Event
        fields = ['title', 'gate_fee', 'location', 'rsvp', 'performer', 'phone', 'email', 'area', 'category',
                  'description', 'start_date', 'end_date', 'image1', 'image2', 'image3', 'image4']
        widgets = {
            'title':forms.TextInput(attrs={'placeholder': 'Event title e.g: Solo night 2015'}),
            'gate_fee':forms.TextInput(attrs={'placeholder': 'Gate fee price in figures e.g: 2000, 0 if free'}),
            'location':forms.TextInput(attrs={'placeholder': 'Physical location of event'}),
            'rsvp':forms.TextInput(attrs={'placeholder': 'Leave blank if none'}),
            'performer':forms.TextInput(attrs={'placeholder': 'Performing artist, leave blank if none'}),
            'phone':forms.TextInput(attrs={'placeholder': 'Organizer\'s phone number'}),
            'email':forms.TextInput(attrs={'placeholder': 'Organizer\'s email'}),
            'description': forms.Textarea(attrs={'placeholder':'Event description, a good and straight description attracts more interest', 'rows':'4'}),
        }

    def save(self, commit=True):
        event = super(EventForm, self).save(commit=False)
        event.active = True
        if event.gate_fee == '':
            event.gate_fee = 0.0
        if commit:
            event.save()
        return event


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'price', 'negotiable', 'location', 'phone', 'email', 'area', 'category', 'description',
                  'image1', 'image2', 'image3', 'image4']
        widgets = {
            'title':forms.TextInput(attrs={'placeholder': 'Service title e.g: Servicing of generators'}),
            'price':forms.TextInput(attrs={'placeholder': 'Price in figures e.g: 2000, 0 if free'}),
            'location':forms.TextInput(attrs={'placeholder': 'Physical location of where the service will be rendered'}),
            'phone':forms.TextInput(attrs={'placeholder': 'Servicer\'s phone number'}),
            'email':forms.TextInput(attrs={'placeholder': 'Servicer\'s email'}),
            'description': forms.Textarea(attrs={'placeholder':'Service description, a good and straight description attracts more interest', 'rows':'4'}),
        }

    def save(self, commit=True):
        service = super(ServiceForm, self).save(commit=False)
        service.active = True
        if service.price == '':
            service.price = 0.0
        if commit:
            service.save()
        return service


class HousingForm(forms.ModelForm):
    class Meta:
        model = Housing
        fields = ['title', 'price', 'negotiable', 'condition', 'duration', 'gender', 'location', 'phone', 'email',
                  'area', 'category', 'description', 'image1', 'image2', 'image3', 'image4']
        widgets = {
            'title':forms.TextInput(attrs={'placeholder': 'Housing title e.g: 3 Bedroom flat for rent'}),
            'price':forms.TextInput(attrs={'placeholder': 'Price in figures e.g: 2000, 0 if free'}),
            'location':forms.TextInput(attrs={'placeholder': 'Physical location of where the building is'}),
            'phone':forms.TextInput(attrs={'placeholder': 'Owner\'s phone number'}),
            'email':forms.TextInput(attrs={'placeholder': 'Owner\'s email'}),
            'description': forms.Textarea(attrs={'placeholder':'Housing description, a good and straight description attracts more interest', 'rows':'4'}),
        }

    def save(self, commit=True):
        housing = super(HousingForm, self).save(commit=False)
        housing.active = True
        if housing.price == '':
            housing.price = 0.0
        if commit:
            housing.save()
        return housing


class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['title', 'price', 'duration', 'location', 'phone', 'email', 'area', 'category', 'description']
        widgets = {
            'title':forms.TextInput(attrs={'placeholder': 'Community title e.g: GNS 101 Tutorials'}),
            'price':forms.TextInput(attrs={'placeholder': 'Price in figures e.g: 2000, 0 if free'}),
            'location':forms.TextInput(attrs={'placeholder': 'Physical location of where the community will take place'}),
            'phone':forms.TextInput(attrs={'placeholder': 'Organizer\'s phone number'}),
            'email':forms.TextInput(attrs={'placeholder': 'Organizer\'s email'}),
            'description': forms.Textarea(attrs={'placeholder':'Community description, a good and straight description attracts more interest', 'rows':'4'}),
        }

    def save(self, commit=True):
        community = super(CommunityForm, self).save(commit=False)
        community.active = True
        if community.price == '':
            community.price = 0.0
        if commit:
            community.save()
        return community


#class ListingForm(forms.ModelForm):
#    class Meta:
#        model = Sale
#        fields = ['title', 'description']
#        widgets = {
#            'title':forms.TextInput(attrs={'placeholder': 'ad title e.g. HP Laptop 630 for sale'}),
#            'description': forms.Textarea(attrs={'placeholder':'ad description, a good and straight description attracts more interest', 'rows':'4'}),
#        }
#
#    def save(self, commit=True):
#        listing = super(ListingForm, self).save(commit=False)
#        listing.active = 1
#        if commit:
#            listing.save()
#        return listing