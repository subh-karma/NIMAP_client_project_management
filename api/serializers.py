from rest_framework import serializers
from .models import Client, Project, ProjectUser
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    client = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = [

{

     'id' : 1,

     'client_name' : 'Nimap',

     'created_at' : '2019-12-24T11:03:55.931739+05:30',

    'created_by' : 'Rohit'

},

{

     'id' : 2,

     'client_name' : 'Infotech',

    'created_at' : '2019-12-24T11:03:55.931739+05:30',

     'created_by' : 'Rohit'

}

]
        