from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, get_object_or_404

from members.models import Member


class HomeView(generic.TemplateView):
    """
    홈 화면
    """
    member = Member
    template_name = 'members/members_info.html'
    paginate_by = 10
    ordering = 'pk'

    def get_queryset(self):
        members = self.member.objects.all().order_by('id')
        return members

    def get(self, request, *args, **kwargs):
        ctx = {
            'view': self.__class__.__name__,  # 클래스의 이름
            'members': self.get_queryset()
        }
        return self.render_to_response(ctx)


class MemberDetailView(generic.DetailView):
    """
    구성원 상세 화면
    """
    model = Member
    template_name = 'members/member_detail.html'
