from django import template
from courses.models import Course

register = template.Library()

@register.simple_tag
def newest_courses():
    '''Gets the most recent courses that were added to the library'''
    Course.objects.latest('created_at')