import re

from rest_framework import serializers

from django.utils import timezone
from django.core.validators import validate_email
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed


from .models import OtpGeneration

User = get_user_model()


class MinifiedUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'email', 'phone_number', 'f_name', 'l_name',)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False, write_only=True, allow_blank=True)
    
    class Meta:
        model = User
        fields = '__all__'

    def validate_email(self, value):
        """
        Only enforce uniqueness if email is provided.
        """
        if value:
            qs = User.objects.filter(email=value)
            if self.instance:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise serializers.ValidationError("This email is already in use.")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    def update(self, instance, validated_data):
        validated_data.pop('password', None)  # Password change handled elsewhere
        return super().update(instance, validated_data)


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['old_password', 'password', 'password2']

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is not correct")
        return value
    
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        old_password = attrs.get('old_password')

        if validate_password(password):
            raise serializers.ValidationError({'password': 'Invalid password format.'})
        
        if password != password2:
            raise serializers.ValidationError({'password2': 'Password not matching.'})
        
        return attrs

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance


class LoginSerializers(TokenObtainPairSerializer):
    """Checks if user has verified email or not"""
    email = serializers.CharField(max_length=256, write_only=True)
    password = serializers.CharField(max_length = 68, min_length=6, write_only=True)

    access = serializers.CharField(max_length=555, read_only=True)
    refresh = serializers.CharField(max_length=555, read_only=True)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # incase we need to add later
        # token['role'] = user.role
        # token['email'] = user.email
        return token

    def validate(self, attrs):
        email = attrs.get('email', '')
        
        user = User.objects.filter(email=email).first()
        
        user = authenticate(**attrs)
        if not user:
            raise AuthenticationFailed('Invalid Credential, Try again')
        
        refresh = self.get_token(user)
        refresh_token = str(refresh)
        access_token = str(refresh.access_token)

        return {
            'access_token': access_token,
            'refresh_token': refresh_token,
        }


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(max_length=256, required=True)


class OTPRequestSerializer(serializers.ModelSerializer):
    # contact = serializers.CharField(write_only=True)
    email = serializers.EmailField(max_length=256, required=False, write_only=True)

    class Meta:
        model = OtpGeneration
        fields = ('otp_code', 'email',)

    def validate(self, attrs):
        # email or phone number
        email = attrs.get('email')
        if not email:
            raise serializers.ValidationError({'error': 'Email is required'})

        email_user = User.objects.filter(email=email).first()

        if not email_user:
            raise serializers.ValidationError({'error': 'User with this email does not exist.'})

        attrs['user'] = email_user

        return super().validate(attrs)
    
    def create(self, validated_data):
        user = validated_data.get('user')
        email = validated_data.get('email')

        OtpGeneration.objects.filter(user=user).delete()
        otp_generation = OtpGeneration.objects.create(user=user)

        # sending email or sms according contact
        # email task here needed template and all
        return 'Done'
    

class OTPVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=256)
    otp_code = serializers.CharField()

    def validate(self, attrs):
        otp_code = attrs.get('otp_code')

        current_date_time = timezone.now()

        email = attrs.get('email')

        user = User.objects.filter(email=email).first()
        if not user:
            raise serializers.ValidationError({'email': 'User with this email does not exist.'})
        
        user_otp_code = OtpGeneration.objects.filter(user=user, otp_code=otp_code).first()

        if not user_otp_code:
            raise serializers.ValidationError({'email': 'OTP code not found for the email.'})
        
        opt_expiry_date_time = user_otp_code.expiry_time

        if current_date_time > opt_expiry_date_time:
            raise serializers.ValidationError({'opt_code': 'OTP code expired.'})
        
        return attrs


class NewPasswordSerializers(serializers.Serializer):
    """Forget password serializer set password"""
    password = serializers.CharField(max_length=68,min_length=8, write_only=True, required=True, validators=[validate_password])
    otp_code = serializers.CharField(min_length=6, write_only=True, required=True)
    email = serializers.EmailField(max_length=256, write_only=True, required=True)

    class Meta:
        fields = ('password', 'otp_code', 'email')
    
    def validate(self, attrs):
        password = attrs.get('password')
        otp_code = attrs.get('otp_code')
        email = attrs.get('email')
    
        current_date_time = timezone.now()

        user = User.objects.filter(email=email).first()
        if not user:
            raise serializers.ValidationError({'email': 'User with this email does not exist.'})

        user_otp_code = OtpGeneration.objects.filter(user=user, otp_code=otp_code).first()

        if not user_otp_code:
            raise serializers.ValidationError({'email': 'Invalid email/otp code'})
        
        opt_expiry_date_time = user_otp_code.expiry_time

        if current_date_time > opt_expiry_date_time:
            raise serializers.ValidationError({'opt_code': 'OTP code expired.'})
        
        user.set_password(password)
        user.save()
        OtpGeneration.objects.filter(user=user, otp_code=otp_code).delete()
        return attrs

