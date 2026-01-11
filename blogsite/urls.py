from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from blog import views as blog_views



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    #path("register/", blog_views.register, name="register"),
     path("password-reset/",auth_views.PasswordResetView.as_view(),name="password_reset",),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
