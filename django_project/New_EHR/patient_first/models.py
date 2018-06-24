from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User



class Patient(models.Model):
    name = models.CharField(max_length=20)
    #date_of_birth = models.DateField
    slugify = models.SlugField(unique=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        self.slug = slugify(self.name)

    class Meta:
        verbose_name_plural = "patients"

    def __str__(self):
        return self.name


class Encounter(models.Model):
    patient = models.ForeignKey(Patient)
    note_type = models.CharField(max_length=20)
    note = models.CharField(max_length=9000)
    signature = models.CharField(max_length=40)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.date

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