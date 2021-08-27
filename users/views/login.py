from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, BlacklistMixin

from users.models import CustomUser
from users.serializers import LoginSerializer, UserSerializer


class LoginViewSet(APIView):
    permission_classes = [AllowAny, ]
    serializer_class = LoginSerializer
    queryset = CustomUser.objects.all()

    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={
            '200': "If user sent correct OTP, endpoint will return user info and token",
            '400': "Bad Request"
        },
        security=[],
        operation_id='LoginUser',
        operation_description='Authenticate Users',
        tags=['Login/Logout'],
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.login_user(request, serializer.validated_data['user']):
            response = UserSerializer(serializer.validated_data['user']).data
            response['tokens'] = self.get_tokens_for_user(serializer.validated_data['user'])
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={'details': 'OTP sent!'}, status=status.HTTP_200_OK)

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
