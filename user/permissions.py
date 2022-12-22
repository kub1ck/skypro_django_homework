from rest_framework.permissions import BasePermission
from user.models import User


class AdPermission(BasePermission):
    message = "Нет прав"

    def has_object_permission(self, request, view, obj):
        # if request.user.id == obj.author_id or request.user.role in (User.ADMIN, User.MODERATOR):
        #     return True
        # else:
        #     return False

        return request.user.id == obj.author_id or request.user.role in (User.ADMIN, User.MODERATOR)
