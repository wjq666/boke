from django.utils import timezone
from rest_framework import serializers

from blogs.apps.system.models import User


class RegisterSerializer(serializers.ModelSerializer):

    username = serializers.CharField(label='用户名')

    class Meta:
        model = User
        fields = ('id', 'username', 'password')

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def validate(self, attrs):
        # 获取username和password
        username = attrs['username']
        password = attrs['password']

        # 进行用户名和密码校验
        try:
            user = User.objects.get(username=username, is_staff=True)
        except User.DoesNotExist:
            raise serializers.ValidationError('用户名或密码错误')
        else:
            # 校验密码
            if not user.check_password(password):
                raise serializers.ValidationError('用户名或密码错误')
        return attrs

