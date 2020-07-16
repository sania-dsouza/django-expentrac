from urllib.parse import urlencode

from django import template

register = template.Library()


@register.simple_tag
def add_index(i):
    return i+1


@register.simple_tag
def get_count(obj_list):
    return range(0, len(obj_list))


@register.filter
def index(obj_list, i):
    return obj_list[i]


@register.filter
def get_attr(obj_list, ele, field):
    return index(obj_list, ele).field


@register.simple_tag
def urlparams(*_, **kwargs):
    safe_args = {k:v for k, v in kwargs.items() if v is not None}
    if safe_args:
        return '?{}'.format(urlencode(safe_args))
    return ''

