from django.db import transaction

from .models import User
from .serializers import UserDataSerializer


def get_request_user_information_service(user: User):
    """"Returns the authenticated user information"""
    return UserDataSerializer(user).data


@transaction.atomic()
def update_user_profile_data(request_data, user: User):
    """"Update the logged in user data using the incoming data"""
    if "first_name" in request_data and request_data["first_name"] is not None:
        user.first_name = request_data["first_name"]
    if "last_name" in request_data and request_data["last_name"] is not None:
        user.last_name = request_data["last_name"]
    if "profile_picture" in request_data and request_data["profile_picture"] is not None:
        user.profile_picture = request_data["profile_picture"]

    user.save()
    return UserDataSerializer(user).data
