from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication


class SpaceAuthentication(BaseAuthentication):
    def authenticate(self, request):
        query_params = request.GET

        if query_params.get("star") == "Sun":
            return User.objects.get(username="nik"), None
