from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_comment(request):
    try:
        response = Response({"result": status.HTTP_200_OK})
        return response
    except Exception as e:
        raise e