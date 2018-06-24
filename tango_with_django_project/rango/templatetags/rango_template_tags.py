from django import template
from rango.models import Patient

register = template.Library()

@register.inclusion_tag('rango/cats.html')
def get_patient_list(cat=None):
    return {'cats': Patient.objects.all(),
            'act_cat': cat}