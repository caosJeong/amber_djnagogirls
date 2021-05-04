from django.conf.urls import url
from django.urls import path
from .views import (
    # 홈화면
    HomeView,
    # 구성원 상세 화면
    MemberDetailView,
    # 구성원 추가 화면
    MemberAddView

)
app_name = 'member'
urlpatterns = [
    url(r'^$',  HomeView.as_view(), name='member_list'),
    url(r'^(?P<pk>\d+)/', MemberDetailView.as_view(), name='member_detail'),
    url(r'^add/$', MemberAddView.as_view(), name='member_add'),
]
