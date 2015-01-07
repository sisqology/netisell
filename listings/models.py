from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from categories.models import SaleCategory, EventCategory, ServiceCategory, HousingCategory, CommunityCategory
from institutions.models import Area


SALE_CONDITION = (
    ('', 'Condition'),
    ('New', 'New'),
    ('Mint', 'Mint'),
    ('Refurbished', 'Refurbished'),
    ('Fairly Used', 'Fairly Used'),
    ('Scrap', 'Scrap'),
)

EVENT_STATUS = (
    ('Active', 'Active'),
    ('Postponed', 'Postponed'),
    ('Cancelled', 'Cancelled'),
)

NEGOTIABLE_CHOICE = (
    ('', 'Negotiable'),
    ('Yes', 'Yes'),
    ('No', 'No')
)

HOUSE_CONDITION = (
    ('', 'Condition'),
    ('Bed Space', 'Bed Space'),
    ('Full Roommate', 'Full Roommate'),
    ('Flat Mate', 'Flat Mate'),
    ('Others', 'Others')
)

HOUSE_DURATION = (
    ('', 'Duration'),
    ('One Week', 'One Week'),
    ('Two Weeks', 'Two Weeks'),
    ('Three Weeks', 'Three Weeks'),
    ('One Month', 'One Month'),
    ('Two Months', 'Two Months'),
    ('Three Months', 'Three Months'),
    ('Four Months', 'Four Months'),
    ('Five Months', 'Five Months'),
    ('Six  Months', 'Six Months'),
    ('One Year', 'One Year'),
    ('Others', 'Others')
)

HOUSE_GENDER = (
    ('', 'Gender'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Any', 'Any'),
)


class Sale(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(null=False)
    price = models.FloatField(null=True, blank=True)
    condition = models.CharField(max_length=50, null=False, blank=False, choices=SALE_CONDITION)
    negotiable = models.CharField(max_length=50, null=False, blank=False, choices=NEGOTIABLE_CHOICE)
    phone = models.CharField(max_length=15, blank=False, null=False)
    email = models.CharField(max_length=50, blank=False, null=False)
    area = models.ForeignKey(Area)
    category = models.ForeignKey(SaleCategory)
    user = models.ForeignKey(User, null=True, blank=False)

    image1 = models.ImageField(upload_to='adverts_images', null=True, blank=True, verbose_name='Advert image')
    image2 = models.ImageField(upload_to='adverts_images', null=True, blank=True, verbose_name='Advert image 2')
    image3 = models.ImageField(upload_to='adverts_images', null=True, blank=True, verbose_name='Advert image 3')
    image4 = models.ImageField(upload_to='adverts_images', null=True, blank=True, verbose_name='Advert image 4')
    small_image = ImageSpecField(source='image1', processors=[ResizeToFill(200, 200)], format='JPEG', options={'quality': 100})
    large_image = ImageSpecField(source='image1', processors=[ResizeToFill(400, 424)], format='JPEG', options={'quality': 100})
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name_plural = "Sales"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Sale, self).save(*args, **kwargs)

    #Not used for now, may be used later. Because of subdomain wildcard urls
    @models.permalink
    def get_absolute_url(self):
        return ('post', (), {'post_id': self.id, 'post_slug': self.slug})
        #return ('ad', [str(self.id), slugify(self.title)])


class Event(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(null=False)
    rsvp = models.CharField(max_length=50, null=False, blank=False)
    status = models.CharField(max_length=50, null=False, blank=False, default='Active', choices=EVENT_STATUS)
    performer = models.CharField(max_length=100, null=True, blank=True)
    gate_fee = models.FloatField(null=True, blank=True)
    location = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=15, blank=False, null=False)
    email = models.CharField(max_length=50, blank=False, null=False)
    area = models.ForeignKey(Area)
    category = models.ForeignKey(EventCategory)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    user = models.ForeignKey(User, null=True, blank=False)
    image1 = models.ImageField(upload_to='adverts_images', null=True, blank=True, verbose_name='Advert image')
    image2 = models.ImageField(upload_to='adverts_images', null=True, blank=True, verbose_name='Advert image 2')
    image3 = models.ImageField(upload_to='adverts_images', null=True, blank=True, verbose_name='Advert image 3')
    image4 = models.ImageField(upload_to='adverts_images', null=True, blank=True, verbose_name='Advert image 4')
    small_image = ImageSpecField(source='image1', processors=[ResizeToFill(200, 200)], format='JPEG', options={'quality': 100})
    large_image = ImageSpecField(source='image1', processors=[ResizeToFill(400, 424)], format='JPEG', options={'quality': 100})
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name_plural = "Events"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Event, self).save(*args, **kwargs)

    #Not used for now, may be used later. Because of subdomain urls
    @models.permalink
    def get_absolute_url(self):
        return ('post', (), {'post_id': self.id, 'post_slug': self.slug})
        #return ('ad', [str(self.id), slugify(self.title)])


class Service(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(null=False)
    negotiable = models.CharField(max_length=50, null=False, blank=False, choices=NEGOTIABLE_CHOICE)
    price = models.FloatField(null=True, blank=True)
    location = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=15, blank=False, null=False)
    email = models.CharField(max_length=50, blank=False, null=False)
    area = models.ForeignKey(Area)
    category = models.ForeignKey(ServiceCategory)
    user = models.ForeignKey(User, null=True, blank=False)
    image1 = models.ImageField(upload_to='adverts_images', null=True, blank=True, verbose_name='Advert image')
    image2 = models.ImageField(upload_to='adverts_images', null=True, blank=True, verbose_name='Advert image 2')
    image3 = models.ImageField(upload_to='adverts_images', null=True, blank=True, verbose_name='Advert image 3')
    image4 = models.ImageField(upload_to='adverts_images', null=True, blank=True, verbose_name='Advert image 4')
    small_image = ImageSpecField(source='image1', processors=[ResizeToFill(200, 200)], format='JPEG', options={'quality': 100})
    large_image = ImageSpecField(source='image1', processors=[ResizeToFill(400, 424)], format='JPEG', options={'quality': 100})
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name_plural = "Services"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Service, self).save(*args, **kwargs)

    #Not used for now, may be used later. Because of subdomain urls
    @models.permalink
    def get_absolute_url(self):
        return ('post', (), {'post_id': self.id, 'post_slug': self.slug})
        #return ('ad', [str(self.id), slugify(self.title)])


class Housing(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(null=False)
    negotiable = models.CharField(max_length=50, null=False, blank=False, choices=NEGOTIABLE_CHOICE)
    condition = models.CharField(max_length=50, null=False, blank=False, choices=HOUSE_CONDITION)
    duration = models.CharField(max_length=20, null=False, blank=False, choices=HOUSE_DURATION)
    gender = models.CharField(max_length=20, null=False, blank=False, default='Any', choices=HOUSE_GENDER)
    price = models.FloatField(null=True, blank=True)
    location = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=15, blank=False, null=False)
    email = models.CharField(max_length=50, blank=False, null=False)
    area = models.ForeignKey(Area)
    category = models.ForeignKey(HousingCategory)
    user = models.ForeignKey(User, null=True, blank=False)
    image1 = models.ImageField(upload_to='adverts_images', null=True, blank=True, verbose_name='Advert image')
    image2 = models.ImageField(upload_to='adverts_images', null=True, blank=True, verbose_name='Advert image 2')
    image3 = models.ImageField(upload_to='adverts_images', null=True, blank=True, verbose_name='Advert image 3')
    image4 = models.ImageField(upload_to='adverts_images', null=True, blank=True, verbose_name='Advert image 4')
    small_image = ImageSpecField(source='image1', processors=[ResizeToFill(200, 200)], format='JPEG', options={'quality': 100})
    large_image = ImageSpecField(source='image1', processors=[ResizeToFill(400, 424)], format='JPEG', options={'quality': 100})
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name_plural = "Housings"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Housing, self).save(*args, **kwargs)

    #Not used for now, may be used later. Because of subdomain urls
    @models.permalink
    def get_absolute_url(self):
        return ('post', (), {'post_id': self.id, 'post_slug': self.slug})
        #return ('ad', [str(self.id), slugify(self.title)])


class Community(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(null=False)
    price = models.FloatField(null=True, blank=True)
    location = models.CharField(max_length=100, null=False, blank=False)
    duration = models.CharField(max_length=20, null=False, blank=False, choices=HOUSE_DURATION)
    phone = models.CharField(max_length=15, blank=False, null=False)
    email = models.CharField(max_length=50, blank=False, null=False)
    area = models.ForeignKey(Area)
    category = models.ForeignKey(CommunityCategory)
    user = models.ForeignKey(User, null=True, blank=False)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name_plural = "Communities"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Community, self).save(*args, **kwargs)

    #Not used for now, may be used later. Because of subdomain urls
    @models.permalink
    def get_absolute_url(self):
        return ('post', (), {'post_id': self.id, 'post_slug': self.slug})
        #return ('ad', [str(self.id), slugify(self.title)])