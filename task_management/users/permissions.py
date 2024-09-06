from rest_framework.permissions import BasePermission

class IsProjectManager(BasePermission):
      def has_permission(self, request, view):
            return request.user.groups.filter(name='Project Manager').exists()
      
class IsDeveloper(BasePermission):
      def has_permission(self, request, view):
            return request.user.groups.filter(name='Developer').exists()
      
class IsAdminOrModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user and (request.user.is_staff or request.user.groups.filter(name='moderators').exists())