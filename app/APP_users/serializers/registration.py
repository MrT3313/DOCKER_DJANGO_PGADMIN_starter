# IMPORTS
from rest_framework import serializers

# MODELS
from APP_users.models.User import User

# MAIN
class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': "password"},
        write_only=True
    )

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            username=self.validated_data['username']
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'passwords must match'})

        user.set_password(password)
        user.save()

        return user