from django.urls import path
from apis.views import UserCreateView, UserLoginView, UserLogoutView

# 여기서 쓰는 url경로는 자바스크립트 json 경로에사용
urlpatterns = [
    path('v1/users/create/',UserCreateView.as_view(), name='apis_v1_user_create' ),
    path('v1/users/login/', UserLoginView.as_view(), name='apis_v1_user_login'),
    path('v1/users/logout/', UserLogoutView.as_view(), name='apis_v1_user_logout'),
]