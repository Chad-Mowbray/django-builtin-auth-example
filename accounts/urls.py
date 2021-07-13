from django.urls import path
from django.contrib.auth import views
from .views import SignUp, CustomLogoutView

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name="accounts/login.html")),
    path('logout/', CustomLogoutView.as_view()),
    path('signup/', SignUp.as_view())
]