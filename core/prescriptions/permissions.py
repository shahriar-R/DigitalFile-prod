# permissions.py
from rest_framework import permissions

class IsDoctor(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated and is a doctor
        return request.user.is_authenticated and request.user.groups.filter(name='Doctor').exists()
