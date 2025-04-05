from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *

# Create your views here.

class UserApiView(APIView):
    def get(self, request):
        allUsers=User.objects.all().values()
        return Response({'Message':"list of users","Users List":allUsers})
    
    def post(self, request):
        User.objects.create(
            username=request.data['username'],
            email=request.data['email'],
            password=request.data['password']
        )

        user=User.objects.all().filter(username=request.data['username']).values()

        return Response({'Message':"New user added","User":user})
    
    def delete(self, request):
        User.objects.all().delete()
        return Response({'Message': "All users deleted successfully"})
    
@api_view(['DELETE'])
def delete_user(request, username,password):
    try:
        user = User.objects.get(username=username,password=password)
        user.delete()
        return Response({'Message':'user deleted successfully'},status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    

