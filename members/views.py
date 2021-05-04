from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views import generic
from django.shortcuts import render, get_object_or_404

from members.models import Member


class HomeView(generic.ListView):
    """
    홈 화면
    """
    model = Member
    ordering = ['id']


class MemberDetailView(generic.DetailView):
    """
    구성원 상세 화면
    """
    model = Member


class MemberAddView(generic.CreateView):
    """
    구성원 추가 화면
    """
    model = Member
    fields = ['member_legs', 'member_name', 'member_gender', 'member_birthday', 'member_description',
              'member_regular', 'member_feature', 'member_feature', 'member_neuter',
              'member_color', 'member_language', 'member_sleep_time', 'member_talent', 'member_img_name', ]
    template_name = 'members/members_form.html'

    def get_success_url(self):
        return reverse('member:member_list')
