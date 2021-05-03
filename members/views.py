from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, get_object_or_404

from members.models import Member


class HomeView(generic.ListView):
    """
    홈 화면
    """
    model = Member
    context_object_name = 'members'  # your own name for the list as a template variable
    queryset = Member.objects.all().order_by('id')  # Get 5 books containing the title war
    template_name = 'members/members_info.html'


class MemberDetailView(generic.DetailView):
    """
    구성원 상세 화면
    """
    model = Member
    template_name = 'members/member_detail.html'


class MemberAddView(generic.CreateView):
    """
    구성원 추가 화면
    """
    model = Member
    fields = ['member_legs', 'member_name', 'member_gender', 'member_birthday', 'member_description',
              'member_regular', 'member_feature', 'member_feature', 'member_neuter',
              'member_color', 'member_language', 'member_sleep_time', 'member_talent', 'member_img_name', ]
    template_name = 'members/members_add.html'
    success_url = "/home"

