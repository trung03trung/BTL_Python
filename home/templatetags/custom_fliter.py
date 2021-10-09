from django import template
from home.models import *
register = template.Library()
@register.filter
def getChilds(catep_id):
    return Category_chile.objects.filter(catep_id=catep_id)