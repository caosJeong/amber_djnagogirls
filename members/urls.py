from django.urls import path
from .views import (
    # 홈화면
    HomeView,
    # 구성원 상세 화면
    MemberDetailView

)

urlpatterns = [
    path('', HomeView.as_view(), name='members_info'),
    path('member/<int:pk>/', MemberDetailView.as_view(), name='member_detail'),
]
