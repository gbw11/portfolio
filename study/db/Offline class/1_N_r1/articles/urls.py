from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
    # 홈페이지 (전체 게시글 조회) - CRUD중 Read
    path('', views.index, name = 'index'),
    # variable routing
    path('<int:pk>/', views.detail, name = 'detail'),
    # 페이지 랜더링 + 리다이렉트
    path('create/', views.create, name = 'create'),
    # 페이지 렌더링 + 리다이렉트
    path('<int:pk>/update/', views.update, name = 'update'),
    path('<int:pk>/delete/', views.delete, name = 'delete'),
    path('<int:pk>/comments/', views.comments_create, name = 'comments_create'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/',
         views.comments_delete, name = 'comments_delete'),
]
