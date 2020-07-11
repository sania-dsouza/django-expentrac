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
def get_attr(ele, field):
    return ele.field
