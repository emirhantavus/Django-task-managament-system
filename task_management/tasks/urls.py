from django.urls import path
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet
from django.conf import settings

router = DefaultRouter()
router.register(r'',TaskViewSet,basename='task')

urlpatterns = [

]
urlpatterns += router.urls