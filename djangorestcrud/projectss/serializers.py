from rest_framework import serializers
from models import Project

class ProjectsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'tecnhology', 'created_at')
        read_only_fields = ('created_at')