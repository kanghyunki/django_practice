from django.urls import path

#.은 현재폴더를 의미하니까, posts에서 views를 가져온다는 말.
from . import views

#이 페이지에 들어오면 views에 있는 index 가져올거야
app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:post_id>/edit/', views.edit, name='edit'),
    path('<int:post_id>/update/', views.update, name='update'),
    path('<int:post_id>/delete/', views.delete, name='delete'),
    path('<int:post_id>/like/', views.like, name='like'),
]



