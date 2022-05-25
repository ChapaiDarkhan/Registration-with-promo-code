from django.urls import re_path
from django.contrib.auth import views as auth_views
from core import views as core_views

urlpatterns = [
    re_path(r'^signup/$', core_views.signup, name='signup'),
    re_path(r'^home$', core_views.home, name='home'),
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(next_page='home'), name="logout"),
    re_path(r'^generate_code/$', core_views.create_invitation_code, name="generate_code"),
]

