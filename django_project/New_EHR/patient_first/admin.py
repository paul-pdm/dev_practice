from django.contrib import admin
from patient_first.models import Patient, Encounter, UserProfile

class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', ]

class EncounterAdmin(admin.ModelAdmin):
    list_display = ['date', ]


admin.site.register(UserProfile)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Encounter, EncounterAdmin)