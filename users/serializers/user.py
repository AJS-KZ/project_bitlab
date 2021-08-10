from rest_framework.serializers import ModelSerializer

from users.models import CustomUser


class UserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'uuid',
            'phone',
            'first_name',
            'last_name',
            'email',
            'created_at',
            'updated_at',
        )
