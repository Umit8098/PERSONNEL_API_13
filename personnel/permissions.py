from rest_framework import permissions

class IsStafforReadOnly(permissions.IsAdminUser):
    message = 'You do not have permission perform this action.'
    
    def has_permission(self, request, view):
       if request.method in permissions.SAFE_METHODS:
           return True
       else:
           return bool(request.user and request.user.is_staff)


class IsOwnerAndStaffOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
           return True
        return bool(request.user.is_staff and (obj.create_user == request.user))
    
    '''
    safe methodlardan ise True dön, 
    eğer 'delete' ise superuser ise true dön, 
    bunun dışında staff ise true dön. 
    '''
    '''
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
           return True
        else:
            if request.method == 'DELETE':
                return bool(request.user.is_superuser)
            return bool(request.user.is_staff)
    '''
