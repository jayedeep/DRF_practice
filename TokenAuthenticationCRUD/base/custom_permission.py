from rest_framework.permissions import BasePermission

class CustomPermission(BasePermission):

    def has_permission(self,request,view):
        if request.method == 'GET' and request.path == '/':  # Logic is that it should
                                                            # give permission to only listing students
            return True
        else:
            return False