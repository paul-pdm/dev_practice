from django.contrib import admin
from rango.models import Patient, Page
from rango.models import UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ['title','patient', 'note']

class PatientAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(UserProfile)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Page, PageAdmin)
