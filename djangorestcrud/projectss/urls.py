from rest_framework import routers
from api import ProjectViewSett

routes = routers.DefaultRouter()

routes.register('api/projects', ProjectViewSett, 'projects')

urlpatterns = routes.urls