from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name="list"),
    path('create/', views.create, name="talk-create"),
    path('update/', views.update, name="talk-update"),
    path('talk/<int:id>/delete/', views.delete, name="talk-delete"),
    path('my_talk/', views.my_talk, name="my_talk"),
    path('talk/<int:id>/', views.detail, name="talk-detail"),
    path('talk/<int:talk_id>/comment/create', views.comment_create, name="comment-create"),
    path('talk/<int:talk_id>/comment/delete/<int:comment_id>', views.comment_delete, name="comment-delete"),
]