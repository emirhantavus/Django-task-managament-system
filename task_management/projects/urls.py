from django.urls import path
from rest_framework.routers import DefaultRouter
from projects.views import ProjectViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'',ProjectViewSet,basename='project')

urlpatterns = [

]
urlpatterns += router.urls