from rest_framework import permissions

class IsadminOrReadonly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff )
    
class FulldjangoPermissin(permissions.DjangoModelPermissions):

    def __str__(self):
       self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']
       

