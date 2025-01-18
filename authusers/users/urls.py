from django.urls import path

from .views import RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    # path("", UserListView.as_view(), name="user_list"),
    # path("create/", UserCreateView.as_view(), name="user_create"),
    # path("<uuid:pk>/", UserDetailView.as_view(), name="user_detail"),
]
