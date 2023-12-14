from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter
def substract(value, arg):
    try:
        return value - arg
    except (ValueError, TypeError):
        return ""
