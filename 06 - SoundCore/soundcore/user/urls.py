from user import views
from django.urls import path

urlpatterns = [
    # path('', views.login_form, name='home'),
    path("login/", views.login_form, name="login_form"),
    path("logout/", views.logout, name="logout"),
    path("accounts_forget/", views.forget_password_form, name="forget_password_form"),
    path("accounts_register/", views.register_form, name="register_form"),
    path("accounts_register/upload_successful/", views.register_success, name="register_success"),
    path("accounts_reset/<str:url>/", views.reset_password_form, name="reset_password"),
]
