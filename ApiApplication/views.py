from django.contrib.auth.hashers import make_password, check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import User, Blog
from .serializer import BlogSerializer

# --- User APIs ---
class UserApiView(APIView):
    def get(self, request):
        users = User.objects.all().values()
        return Response({'message': "List of users", 'users': users})

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email', '')
        password = request.data.get('password')

        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                return Response({
                    'message': f"Welcome back, {username}!",
                    'user': {'username': user.username, 'email': user.email}
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Incorrect password'}, status=status.HTTP_401_UNAUTHORIZED)

        except User.DoesNotExist:
            hashed_password = make_password(password)
            new_user = User.objects.create(
                username=username,
                email=email,
                password=hashed_password
            )
            return Response({
                'message': f"New user {username} signed up successfully.",
                'user': {'username': new_user.username, 'email': new_user.email}
            }, status=status.HTTP_200_OK)

    def delete(self, request):
        User.objects.all().delete()
        return Response({'message': "All users deleted successfully"})


@api_view(['DELETE'])
def delete_user(request, username, password):
    try:
        user = User.objects.get(username=username)
        if check_password(password, user.password):
            user.delete()
            return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'Incorrect password'}, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


# --- Blog APIs ---
class BlogApiView(APIView):
    def get(self, request):
        blogs = Blog.objects.all().values()
        return Response({'message': "List of all blogs", 'blogs': blogs})

    def post(self, request):
        username = request.data.get('username')
        title = request.data.get('title')
        content = request.data.get('content')

        try:
            user = User.objects.get(username=username)
            blog = Blog.objects.create(title=title, content=content, created_by=user)
            return Response({
                'message': 'Blog created successfully!',
                'blog': {
                    'id': blog.id,
                    'title': blog.title,
                    'content': blog.content,
                    'author': blog.created_by.username
                }
            }, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({'error': 'Invalid user'}, status=status.HTTP_404_NOT_FOUND)


class BlogDetailApiView(APIView):
    def get(self, request, blog_id):
        username = request.GET.get('username')

        try:
            blog = Blog.objects.get(id=blog_id)
            if blog.created_by.username != username:
                return Response({'error': 'You are not allowed to view this blog'}, status=status.HTTP_403_FORBIDDEN)

            return Response({'blog': {
                'id': blog.id,
                'title': blog.title,
                'content': blog.content,
                'username': blog.created_by.username
            }})
        except Blog.DoesNotExist:
            return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, blog_id):
        username = request.data.get('username')
        title = request.data.get('title')
        content = request.data.get('content')

        try:
            blog = Blog.objects.get(id=blog_id)
            if blog.created_by.username != username:
                return Response({'error': 'You are not allowed to edit this blog'}, status=status.HTTP_403_FORBIDDEN)

            blog.title = title
            blog.content = content
            blog.save()
            return Response({'message': 'Blog updated successfully'})
        except Blog.DoesNotExist:
            return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, blog_id):
        username = request.data.get('username')

        try:
            blog = Blog.objects.get(id=blog_id)
            if blog.created_by.username != username:
                return Response({'error': 'You are not allowed to delete this blog'}, status=status.HTTP_403_FORBIDDEN)

            blog.delete()
            return Response({'message': 'Blog deleted successfully'})
        except Blog.DoesNotExist:
            return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_all_blogs(request):
    username = request.data.get('username')
    if not username:
        return Response({'error': 'Username required'}, status=status.HTTP_400_BAD_REQUEST)

    deleted_count, _ = Blog.objects.filter(created_by__username=username).delete()
    return Response({'message': f'All {deleted_count} blog(s) by {username} deleted successfully'})
