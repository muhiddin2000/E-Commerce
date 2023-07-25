from .models import CustomUser
from rest_framework.serializers import (ModelSerializer, ValidationError, SerializerMethodField,
                                        HyperlinkedModelSerializer)


class UserSerializer(HyperlinkedModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser.objects.create(**validated_data)
        if password:
            user.set_password(password)
            user.save()

        return user

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')

    extra_kwargs = {"password":
                        {"write_only": True}
                    }

    def to_representation(self, ins):
        return {
            "id": ins.id,
            "username": ins.username,
            "first_name": ins.first_name,
            "last_name": ins.last_name,
            "email": ins.email
        }


class UserUpdateSerializers(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ( 'username', 'first_name', 'last_name', 'email')