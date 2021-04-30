import re

from django import template

register = template.Library()


@register.filter
def legs_hashtag_str(value):
    content = '#{} #{} #{}'.format(value.legs_type, value.legs_sub1_type, value.legs_sub2_type)
    return content  # 원하는 문자열로 치환이 완료된 content를 리턴한다.


@register.filter
def boolean_str(value):
    if value:
        content = "YES"
    else:
        content = "NO"

    return content  # 원하는 문자열로 치환이 완료된 content를 리턴한다.
