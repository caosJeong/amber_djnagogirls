from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from members.forms import MemberFrom, MemberUpdateFrom
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


class MemberAddView(CreateView):
    """
    구성원 추가 화면
    """
    form_class = MemberFrom
    template_name = 'members/member_form.html'

    def get_success_url(self):
        return reverse('member:member_list')

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))


class MemberUpdateView(UpdateView):
    """
    구성원 수정 화면
    """
    model = Member
    form_class = MemberUpdateFrom
    template_name = 'members/member_update.html'


class MemberDeleteView(DeleteView):
    """
    구성원 삭제 화면
    """
    model = Member

    def get_success_url(self):
        return reverse('member:member_list')
