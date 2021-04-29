from django.urls import path
from .views import (
    # 홈화면
    HomeView

)

urlpatterns = [
    path('', HomeView.as_view(), name='members_info'),
]
