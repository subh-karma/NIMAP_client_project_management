from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Client, Project, ProjectUser
from .serializers import ClientSerializer, ProjectSerializer
from django.shortcuts import get_object_or_404
from django.db import transaction

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=['post'])
    @transaction.atomic
    def projects(self, request, pk=None):
        client = self.get_object()
        project_data = request.data
        
        project = Project.objects.create(
            project_name=project_data['Nimap'],
            client=client,
            created_by=request.user
        )
        
        if 'users' in project_data:
            user_ids = [user['id'] for user in project_data['users']]
            for user_id in user_ids:
                ProjectUser.objects.create(
                    project=project,
                    user_id=user_id
                )
        
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(users=self.request.user)