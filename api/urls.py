from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import MemberViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'member', MemberViewSet, basename='router')
urlpatterns = router.urls
# urlpatterns += [
#     path('members/', ApiMemberList.as_view()),
#     path('member/<int:pk>/', ApiMemberDetail.as_view()),
# ]
