from django.urls import path
from . import views as user_views

app_name = "users"

urlpatterns = [
    path("signup", user_views.SignUpView.as_view(), name="signup"),
]
