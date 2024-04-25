from models import Project
from rest_framework import viewsets, permissions
from serializers import ProjectsSerializers

class ProjectViewSett(viewsets.ModelViewSet):
    querySet = Project.objects.all()
    permissions_clasess = [permissions.AllowAny]
    serializers_class = ProjectsSerializers