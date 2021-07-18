# IMPORTS
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# MODELS
from rest_framework.authtoken.models import Token

# SERIALIZERS
from APP_users.serializers.registration import RegistrationSerializer

# MAIN
@api_view(['POST'])
@permission_classes([AllowAny])
def register_new_user(req):
    serializer = RegistrationSerializer(data=req.data)
    data = {}

    if serializer.is_valid():
        # SAVE: new user
        user = serializer.save()

        # GET: generated token (post_save signal on User)
        token = Token.objects.get(user=user).key

        # UPDATE: response
        data['token'] = token

    else:
        # UPDATE: response to serializer error
        data = serializer.errors

    # RETURN
    return Response(data)