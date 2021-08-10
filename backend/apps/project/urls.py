from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include

from project import views

app_name = "project"

router = DefaultRouter()

router.register(r'', views.ProjectView, basename="base")

urlpatterns = [
    url(r'^', include(router.urls)),
]
