import uuid
import random

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

from django.db import models

from utils.custom_models import CustomBaseModel

from .enums import UserRoleChoices


class CustomUserManager(BaseUserManager):
    def create_user(self, role: str, email: str, password=None, **kwargs):
        email = self.normalize_email(email) if email else None
        user = self.model(role=role, email=email, **kwargs)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user

    def create_superuser(self, email: str, password=None):
        if not password:
            raise TypeError("Superuser must have a password")
        user = self.create_user(
            role=UserRoleChoices.SUPER_ADMIN,
            password=password,
            email=email
        )
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    f_name = models.CharField(max_length=200, null=True, blank=True)
    l_name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)


    email = models.EmailField(max_length=256, db_index=True, unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    role = models.CharField(max_length=3, choices=UserRoleChoices.choices, default=UserRoleChoices.USER)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ['f_name', 'l_name']

    @property
    def is_admin(self):
        return self.role == UserRoleChoices.ADMIN
    
    @property
    def is_staff_member(self):
        return self.role in [
            UserRoleChoices.STAFF,
            UserRoleChoices.ADMIN,
            UserRoleChoices.SUPER_ADMIN
        ]
    
    def get_full_name(self):
        """
        Returns the full name of the user.
        """
        return f"{self.f_name or ''} {self.l_name or ''}".strip()

    def __str__(self):
        return f"{self.email}"

    @property
    def full_name(self):
        return f"{self.f_name or ''} {self.l_name or ''}".strip()


def generate_unique_otp_number():
    # this will only be used for opening quantity batch creation
    random_number = random.randint(111111,999999)
    while OtpGeneration.objects.filter(otp_code=random_number).exists():
        random_number = random.randint(111111,999999)
    return random_number


def default_expiry_date_time():
    # set the expiry date to 30 mins more then current date time
    return timezone.now() + timezone.timedelta(minutes=30)


class OtpGeneration(CustomBaseModel):
    # 1 otp per user should be present for the user it that token is used already then token will not be valid
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6, unique=True, default=generate_unique_otp_number)
    expiry_time = models.DateTimeField(default=default_expiry_date_time)

    def __str__(self) -> str:
        return self.otp_code

