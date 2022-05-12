# For translation purpose
from django.utils.translation import gettext_lazy as _
from django.db import models

# For the Custom user
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# to specify a range
from django.core.validators import MinValueValidator, MaxValueValidator


class ResearcherUserManager(BaseUserManager):
    """
    The Manager of the user(Researcher)
    """

    def create_user(self, full_name, email, password=None, **other_fields):
        """
        Simple user
        """
        if not email:
            raise ValueError(_("the email must be set "))
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, full_name, email, password=None, **other_fields):
        """
        Superuser(admin)
        """
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError("Superuser must be is_staff")

        if other_fields.get('is_active') is not True:
            raise ValueError("Superuser must be is_active")

        if other_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must be is_superuser")
        return self.create_user(full_name, email, password, **other_fields)


# custom user
class Researcher(AbstractBaseUser, PermissionsMixin):
    """
    The user profile of a researcher 
    """
    joined = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=150, unique=True)
    email = models.EmailField(_('email adress'), unique=True)
    speciality = models.CharField(max_length=150, blank=True)
    grade = models.CharField(max_length=200, blank=True)
    twitter_account = models.URLField(blank=True)
    linkedin_account = models.URLField(blank=True)
    google_scholar_account = models.URLField(blank=True)

# Relationship between Database tables
    # Location --> Wilaya : A location table
    location = models.ForeignKey(
        'Location', on_delete=models.SET_NULL, null=True
    )

    # affiliations = models.CharField(max_length=150)

    # interests

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = ResearcherUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    class Meta:
        ordering = ['joined']

    def __str__(self) -> str:
        return self.full_name


class Location(models.Model):
    state_name = models.CharField(max_length=30)
    state_number = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(58)]
    )

    def __str__(self) -> str:
        return self.state_name
