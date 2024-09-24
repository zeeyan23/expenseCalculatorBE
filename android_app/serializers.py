from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(many=True, read_only='True')
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True
    )
    email = serializers.CharField(
        style={'input_type': 'email'}, write_only=True
    )
    groups = serializers.CharField(
        style={'input_type': 'text'}, write_only=True
    )

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'password', 'groups']
        


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ['url', 'id', 'name']

class all_records(serializers.ModelSerializer):
    class Meta:
        model=all_records
        fields=['id','name','price','credited_date','createdDate','modifiedDate']