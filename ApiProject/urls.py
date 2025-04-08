from django.contrib import admin
from django.urls import path
from ApiApplication.views import UserApiView, delete_user, BlogApiView, BlogDetailApiView ,delete_all_blogs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', UserApiView.as_view()),
    path('api/user/delete-user/<str:username>/<str:password>/', delete_user, name='delete_user'),

    path('api/blogs/', BlogApiView.as_view()),
    path('api/blogs/<int:blog_id>/', BlogDetailApiView.as_view()),
    path('api/blogs/delete_all/', delete_all_blogs, name='delete_all_blogs'),
]
