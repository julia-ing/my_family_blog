from django.urls import path
from . import views

urlpatterns = [
    path('posting_list/', views.posting_list, name="posting_list"),
    path('posting_list_info/<int:pk>', views.posting_list_info, name="posting_list_info"),
    path('comment_remove/<int:pk>', views.comment_remove, name="comment_remove"),
    path('create_posting/', views.create_posting, name="create_posting"),
    path('my_posting/', views.my_posting, name="my_posting"),
    path('edit_posting/<int:pk>', views.edit_posting, name="edit_posting"),
]
