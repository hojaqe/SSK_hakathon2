from rest_framework import serializers
from django.contrib.auth import get_user_model
from .utils import send_activation_code
from .models import User

User = get_user_model()

class RegistrationSerializers(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=4, required=True)
    password_confirm = serializers.CharField(min_length=4, required=True)
    name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=False)
   
    

# class ActivationSerializer(serializers.Serializer):
#     email = serializers.CharField()
#     code = serializers.CharField()

#     def validate(self, attrs):
#         email = attrs.get('email')
#         code = attrs.get('code')
#         if not User.objects.filter(email=email, activation_code=code).exists():
#            raise serializers.ValidationError('Пользователь не найден')
#         return attrs
    
#     def activate(self):
#         email = self.validated_data.get('email')
#         user = User.objects.get(email=email)
#         user.is_active = True
#         user.activation_code = ''
#         user.save()



class RegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


# class ActivationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = "__all__"
