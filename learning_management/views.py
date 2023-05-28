import os
from datetime import datetime

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, authentication_classes


@api_view(http_method_names=["POST"])
@authentication_classes([])
@permission_classes([])
def session_auth(request: Request):
    data = request.data

    user = authenticate(username=data["username"], password=data["password"])

    if user:
        login(request, user)
        return Response(user.username)
    else:
        return Response("Unauthorized", status=401)


def now_page(request):
    now = datetime.now()

    return HttpResponse(now)
