from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('post/add/', views.PostAdd.as_view(), name='post_add'),
    path('<slug:slug>/update/', views.PostUpdate.as_view(),
         name='post_update'),
    path('<slug:slug>/delete/', views.PostDelete.as_view(),
         name='post_delete'),
]
