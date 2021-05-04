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
    path('',  HomeView.as_view(), name='member_list'),
    path('<int:pk>/', MemberDetailView.as_view(), name='member_detail'),
    path('add/', MemberAddView.as_view(), name='member_add'),
]
