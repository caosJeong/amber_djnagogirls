from django.conf.urls import url
from django.urls import path
from .views import (
    # 구성원 목록
    HomeView,
    # 구성원 상세, 추가, 수정, 삭제 화면
    MemberDetailView,
    MemberAddView,
    MemberUpdateView,
    MemberDeleteView,

)
app_name = 'member'
urlpatterns = [
    path('',  HomeView.as_view(), name='member_list'),
    path('<int:pk>/', MemberDetailView.as_view(), name='member_detail'),
    path('add/', MemberAddView.as_view(), name='member_add'),
    path('update/<int:pk>/', MemberUpdateView.as_view(), name='member_update'),
    path('delete/<int:pk>/', MemberDeleteView.as_view(), name='member_delete'),
]
