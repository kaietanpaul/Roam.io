from django import template

register = template.Library()


# The get_item Django template filter retrieves a value from a dictionary by key,
# providing a convenient way to access dictionary items in templates.
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
