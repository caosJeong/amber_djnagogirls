from django.shortcuts import render
from django.views import generic

from members.models import Member


class HomeView(generic.TemplateView):
    """
    홈 화면
    """
    member = Member
    template_name = 'members/members_info.html'
    paginate_by = 10
    ordering = '-pk'

    def get_queryset(self):
        members = self.member.objects.all()
        return members[:self.paginate_by]

    def get(self, request, *args, **kwargs):
        ctx = {
            'view': self.__class__.__name__,  # 클래스의 이름
            'members': self.get_queryset()
        }
        return self.render_to_response(ctx)

