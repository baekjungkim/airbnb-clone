from django.urls import path
from . import views as core_views
from rooms import views as room_views

app_name = "core"

urlpatterns = [
    path("", room_views.HomeView.as_view(), name="home"),
    path("login", core_views.LoginView.as_view(), name="login"),
    path("logout", core_views.log_out, name="logout"),
]
