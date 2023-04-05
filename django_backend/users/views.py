from django.views.decorators.http import require_http_methods
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import UserDataSerializer
from .services import get_request_user_information_service, update_user_profile_data


# GET Methods

@swagger_auto_schema(
    method='GET',
    responses={
        200: UserDataSerializer()
    }
)
@require_http_methods(["GET"])
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_data(request):
    try:
        response = get_request_user_information_service(user=request.user)
        return Response(data=response, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# PUT methods

@swagger_auto_schema(
    method='PUT',
    responses={
        200: UserDataSerializer()
    }
)
@require_http_methods(["PUT"])
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_data(request):
    try:
        response = update_user_profile_data(request_data=request.data, user=request.user)
        return Response(data=response, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
