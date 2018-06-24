from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Patient(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Patient, self).save(*args, **kwargs)

    @property
    def pages(self):
        pages = self.page_set.all()
        return Page.objects.filter(page_set__in=pages)

    class Meta:
            verbose_name_plural = "patients"

    def __str__(self):
        return self.name

class Page(models.Model):
    patient = models.ForeignKey(Patient)
    title = models.CharField(max_length=128)
    note = models.CharField(max_length=2000)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    # Remember if your use Python 2.7.x, define __unicode__ too!
    def __str__(self):
        return self.user.username
