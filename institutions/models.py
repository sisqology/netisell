from django.db import models


class Institution(models.Model):
    fullname = models.CharField(max_length=200, blank=False, null=False)
    abbr = models.CharField(max_length=50, blank=False, null=False)

    def __unicode__(self):
        return self.abbr

    class Meta:
        ordering = ('abbr',)

    def save(self, *args, **kwargs):
        super(Institution, self).save(*args, **kwargs)


class Area(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    institution = models.ForeignKey(Institution)

    def __unicode__(self):
        return '%s - %s' %(self.name, self.institution)

    class Meta:
        ordering = ('name',)

    def save(self, *args, **kwargs):
        super(Area, self).save(*args, **kwargs)