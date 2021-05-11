from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from members.forms import MemberFrom
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_list'] = self.object.assign.all()
        context['watcher_list'] = self.object.watcher.values('todo_title', 'todo_assign__member_name')
        return context


class MemberAddView(CreateView):
    """
    구성원 추가 화면
    """

    form_class = MemberFrom
    template_name = 'members/member_form.html'

    def get_success_url(self):
        return reverse('member:member_detail', kwargs={'pk': self.object.id})


class MemberUpdateView(UpdateView):
    """
    구성원 수정 화면
    """
    model = Member
    form_class = MemberFrom
    template_name = 'members/member_update.html'

    def get_success_url(self):
        return reverse('member:member_detail', kwargs={'pk': self.object.id})


class MemberDeleteView(DeleteView):
    """
    구성원 삭제 화면
    """
    model = Member

    def get_success_url(self):
        return reverse('member:member_list')
