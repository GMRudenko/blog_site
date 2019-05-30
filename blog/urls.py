from django.urls import path
from . import views
from django.conf.urls import url
from django.urls import include

urlpatterns = [
    url(r'^$', views.index),
    path('post/<int:pk>', views.MainPostView, name='mainpost-detail'),
    path('all_posts/', views.MainPostListView.as_view(), name='all-posts'),
    path('create_post/', views.MainPostCreate, name='mainpost-create'),

]
