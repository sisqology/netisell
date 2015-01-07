from django.db import models
from django.template.defaultfilters import slugify


class SaleCategory(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(blank=True, null=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s' %(self.name)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Sale Categories"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SaleCategory, self).save(*args, **kwargs)


class EventCategory(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(blank=True, null=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s' %(self.name)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Event Categories"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(EventCategory, self).save(*args, **kwargs)


class ServiceCategory(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(blank=True, null=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s' %(self.name)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Service Categories"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ServiceCategory, self).save(*args, **kwargs)


class HousingCategory(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(blank=True, null=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s' %(self.name)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Housing Categories"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(HousingCategory, self).save(*args, **kwargs)


class CommunityCategory(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(blank=True, null=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s' %(self.name)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Community Categories"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(CommunityCategory, self).save(*args, **kwargs)