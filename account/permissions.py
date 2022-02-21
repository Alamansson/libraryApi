from rest_framework.permissions import BasePermission


class IsAuthorPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        # print('USER and AUTHOR', request.user, obj.publisher)
        # print("REQUEST", request)
        # print("REQUEST DATA", request.data)
        # print("OBJECT", obj)
        return obj.publisher == request.user


class IsActive(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_active)


