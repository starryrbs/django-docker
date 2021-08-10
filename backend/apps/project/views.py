from rest_framework import mixins, viewsets

from project.models import Project
from project.serializers import ProjectSerializer


class ProjectView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
