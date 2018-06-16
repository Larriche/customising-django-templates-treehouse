from django import template
from courses.models import Course

register = template.Library()

@register.simple_tag
def newest_course():
    '''Gets the most recent course that was added to the library'''
    return Course.objects.latest('created_at')

@register.inclusion_tag('courses/course_nav.html')
def nav_courses_list():
    '''Return dictionary of courses to display as a navigation pane'''
    courses = Course.objects.all()
    return {'courses': courses}
