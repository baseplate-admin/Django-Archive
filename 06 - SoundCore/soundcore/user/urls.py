from user import views
from django.urls import path

urlpatterns = [
    # path('', views.login_form, name='home'),
    path("login.py", views.login_form, name="login_form"),
    path("logout.py", views.logout, name="logout"),
    path("forget.py", views.forget_password_form, name="forget_password_form"),
    path("register.py", views.register_form, name="register_form"),
    path("register/successful.py", views.register_success, name="register_success"),
    path("reset/<str:url>.py", views.reset_password_form, name="reset_password"),
]
