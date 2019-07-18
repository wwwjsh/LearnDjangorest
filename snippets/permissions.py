from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    常规的授权是 只有拥有者才能编辑它
    '''

    def has_object_permission(self, request, view, obj):
        # 读权限 向所有请求开放
        # 所以我们总是允许get, head or options requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # 写权限 只给拥有者
        return obj.owner == request.user


