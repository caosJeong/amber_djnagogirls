from django import forms
from .models import Member


class MemberFrom(forms.ModelForm):
    error_css_class = 'w3-text-red'

    class Meta:
        model = Member
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.id is not None:
            self.fields['member_legs'].widget.attrs['class'] = 'w3-text-gray'
            self.fields['member_name'].widget.attrs['class'] = 'w3-text-gray'
        else:
            self.fields['member_description'].widget.attrs['placeholder'] = '구성원의 특징을 입력 해 주세요'
            self.fields['member_feature'].widget.attrs['placeholder'] = '구성원의 특징을 입력 해 주세요'
