from django import template, forms
from django.db.models import ImageField

register = template.Library()

@register.filter(name="isImageField")
def isImageField(instance):
    return isinstance(instance.field.field, forms.fields.ImageField)