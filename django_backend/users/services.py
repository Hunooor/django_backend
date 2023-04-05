from .models import User
from .serializers import UserDataSerializer


def get_request_user_information_service(user: User):
    """"Returns the authenticated user information"""
    return UserDataSerializer(user).data

