from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from institutions.models import Area, Institution
from datetime import date


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(blank=True, null=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s' %(self.name)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Discussion Categories"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Topic(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(blank=True, null=True)
    topic_comment = models.TextField(blank=False, null=False, verbose_name='Comment')
    institution = models.ForeignKey(Institution, blank=False, null=False)
    category = models.ForeignKey(Category, null=False, blank=False)
    user = models.ForeignKey(User, null=False, blank=False)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, editable=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-date_created',)
        verbose_name_plural = "Topics"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Topic, self).save(*args, **kwargs)

    #Not used for now, may be used later. Because of subdomain urls
    @models.permalink
    def get_absolute_url(self):
        return ('topic', (), {'topic_id': self.id, 'topic_slug': self.slug})
        #return ('ad', [str(self.id), slugify(self.title)])


class Comment(models.Model):
    comment = RichTextField()
    topic = models.ForeignKey(Topic)
    user = models.ForeignKey(User, null=False, blank=False)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, editable=True)

    def __unicode__(self):
        return self.comment

    class Meta:
        ordering = ('date_created',)
        verbose_name_plural = "Comments"

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)