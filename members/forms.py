from django import forms
from django.core.exceptions import ValidationError

from .models import Member


class MemberFrom(forms.ModelForm):
    error_css_class = 'w3-text-red'

    class Meta:
        model = Member
        # fields = ['member_legs', 'member_name', 'member_gender', 'member_birthday', 'member_description',
        #           'member_regular', 'member_feature', 'member_feature', 'member_neuter',
        #           'member_color', 'member_language', 'member_sleep_time', 'member_talent', 'member_img_name', ]
        fields = '__all__'


class MemberUpdateFrom(MemberFrom):
    class Meta(MemberFrom.Meta):
        widgets = {
            'member_legs': forms.Select(attrs={'disabled': 'true'}),
            'member_name': forms.TextInput(attrs={'disabled': 'true'}),
        }
