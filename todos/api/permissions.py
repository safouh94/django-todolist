from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    message = 'you must be the owner of the object'
    my_safe_method = ['GET', 'PUT']

    def has_permission(self, request, view):
        if request.method in self.my_safe_method:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # member = Membership.objects.get(user=request.uesr)
        # member.is_active
        # if request.method in self.my_safe_method:
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
