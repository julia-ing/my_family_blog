from django.urls import path
from . import views

urlpatterns = [
    path('lecture_list/', views.lecture_list, name="lecture_list"),
    path('lecture_list_info/<int:pk>', views.lecture_list_info, name="lecture_list_info"),
    path('comment_remove/<int:pk>', views.comment_remove, name="comment_remove"),
    path('create_lecture/', views.create_lecture, name="create_lecture"),
    path('my_lecture/', views.my_lecture, name="my_lecture"),
    path('edit_lecture/<int:pk>', views.edit_lecture, name="edit_lecture"),
]
