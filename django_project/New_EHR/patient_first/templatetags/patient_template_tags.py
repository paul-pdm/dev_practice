from django import template
from patient_first.models import Patient

register = template.Library()

@register.inclusion_tag('patient_first/pats.html')
def get_patient_list(pat=None):
    return {'pats' : Patient.objects.all(),
            'act_pat': pat}