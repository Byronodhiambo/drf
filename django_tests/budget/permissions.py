from rest_framework import permissions


class IsStaffEditorPermissionn(permissions.DjangoModelPermissions):

    def has_permission(self, request, view):

        perms_map = {
            'GET': ['%(app_label)s.view_%(model_name)s'],
            'OPTIONS': [],
            'HEAD': [],
            'POST': ['%(app_label)s.add_%(model_name)s'],
            'PUT': ['%(app_label)s.change_%(model_name)s'],
            'PATCH': ['%(app_label)s.change_%(model_name)s'],
            'DELETE': ['%(app_label)s.delete_%(model_name)s'],
        }

        if not request.user.is_staff:
            return False
        return super().has_permission(request, view)

        # user = request.user
        # print(user.get_all_permissions())
        # if user.is_staff:
        #     if user.has_perm("budget.add_project"):
        #         return True
        #     if user.has_perm("budget.change_project"):
        #         return True
        #     if user.has_perm("budget.delete_project"):
        #         return True
        #     if user.has_perm("budget.view_project"):
        #         return True
            