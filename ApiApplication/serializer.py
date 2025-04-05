from rest_framework import serializers

from .models import User

class UserSerilizers(serializers.ModelSerializer):


    class Meta:
        model=User
        fields=('id', 'username', 'email','password')