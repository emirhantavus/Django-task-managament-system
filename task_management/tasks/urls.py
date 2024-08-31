from django.urls import path
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet , TaskCompleteView
from django.conf import settings

router = DefaultRouter()
router.register(r'',TaskViewSet,basename='task')

urlpatterns = [
      path('tasks/<int:pk>/complete/', TaskCompleteView.as_view(), name='task-complete'),
]
urlpatterns += router.urls