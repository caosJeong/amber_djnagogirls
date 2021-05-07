from django.urls import path
from .views import (
    ApiMemberList,
    ApiMemberDetail

)

urlpatterns = [
    path('members/', ApiMemberList.as_view()),
    path('member/<int:pk>/', ApiMemberDetail.as_view()),
]
