from django.contrib.auth.hashers import make_password, check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import User

class UserApiView(APIView):
    def get(self, request):
        allUsers = User.objects.all().values()
        return Response({'message': "List of users", "users": allUsers})

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
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
