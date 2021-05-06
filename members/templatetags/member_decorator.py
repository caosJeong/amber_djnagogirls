import math
import re

from django import template

register = template.Library()


@register.filter
def legs_hashtag_str(value):
    content = f'#{value.legs_type} #{value.legs_sub1_type} #{value.legs_sub2_type}'
    return content


@register.filter
def boolean_str(value):
    if value:
        content = "YES"
    else:
        content = "NO"

    return content


@register.filter()
def block_object_list(object_list, block_size=3):
    object_list2 = []
    for i in range(0, math.ceil(len(object_list) / block_size)):
        object_list2.append(object_list[i * block_size:(i * block_size) + block_size])

    return object_list2
