from django.urls import path
from .views import delete_comment, delete_post, home, blog_list, about, post_detail, toggle_like

urlpatterns = [
    path("", home, name="home"),
    path("blogs/", blog_list, name="blogs"),
    path("about/", about, name="about"),
    path("post/<slug:slug>/", post_detail, name="post_detail"),
    path("post/<slug:slug>/like/", toggle_like, name="toggle_like"),
    path("comment/<int:comment_id>/delete/", delete_comment, name="delete_comment"),
    path("post/<slug:slug>/delete/", delete_post, name="delete_post"),

]
