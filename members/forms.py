from django import forms
from .models import Member


class MemberFrom(forms.ModelForm):
    error_css_class = 'w3-text-red'

    class Meta:
        model = Member
        fields = '__all__'

    def __init__(self, member=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if isinstance(member, Member):
            self.fields['member_legs'].widget.attrs['disabled'] = 'true'
            self.fields['member_name'].widget.attrs['disabled'] = 'true'
        else:
            self.fields['member_description'].widget.attrs['placeholder'] = '구성원의 특징을 입력 해 주세요'
            self.fields['member_feature'].widget.attrs['placeholder'] = '구성원의 특징을 입력 해 주세요'
