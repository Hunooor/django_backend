from django.views.decorators.http import require_http_methods
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@swagger_auto_schema(
    method='GET'
)
@require_http_methods(["GET"])
@api_view(['GET'])
def check_server_endpoint(request):
    return Response(status=status.HTTP_200_OK)
