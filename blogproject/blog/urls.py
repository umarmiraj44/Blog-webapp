from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list,name='postlist'),
    path('delete/<int:postid>',views.postdelete,name='postdelete'),
]