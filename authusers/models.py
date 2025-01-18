from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework_simplejwt.tokens import RefreshToken

from drf_catalyst.models import AbstractBaseModel


class UserRole(models.TextChoices):
    SUPERUSER = "SU", "Super User"
    ADMIN = "AD", "Admin"
    USER = "UR", "User"


class UserManager(BaseUserManager):
    def create_user(self, username=None, email=None, password=None):
        if not (username or password):
            raise TypeError("Users must have a username or email.")
        user = self.model(username=username, email=email)
        user.is_active = True
        user.save()
        user.set_password(password)
        return user

    def create_superuser(self, username, password, email=None):
        if password is None:
            raise TypeError("Superusers must have a password.")
        user = self.create_user(username, email, password)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

    def from_email(self, email):
        return self.filter(email=email).first

    def from_username(self, username):
        return self.filter(username=username).first

    def from_username_or_email(self, username_or_email):
        return self.filter(
            models.Q(username=username_or_email) | models.Q(email=username_or_email)
        ).first()


class User(AbstractBaseUser, AbstractBaseModel, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    role = models.CharField(
        max_length=2,
        choices=UserRole.choices,
        default=UserRole.USER,
    )
    is_active = models.BooleanField(
        default=False,
        help_text="Inactive users can not log into the system.",
    )
    is_staff = models.BooleanField(
        default=False,
        help_text="staffs can access django admin panel with assigned permissions.",
    )
    is_superuser = models.BooleanField(default=False)  # superuser privilege
    deletion_initiated_at = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = "username"

    objects: UserManager = UserManager()

    def get_refresh_token(self):
        return RefreshToken.for_user(self)


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        db_index=True,
        editable=False,
    )
    first_name = models.CharField(max_length=200, null=True, blank=True)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to="profile-picture/",
        null=True,
        blank=True,
    )
    address = models.CharField(max_length=200, null=True, blank=True)
    phone_number = PhoneNumberField(region="NP", unique=True)

    def __str__(self) -> str:
        return f"{self.full_name}"

    @property
    def full_name(self):
        if self.first_name is None or self.first_name == "":
            return self.user.email
        return (
            f"{self.first_name} {self.middle_name} {self.last_name}".replace("None", "")
            .replace("  ", " ")
            .strip()
        )
