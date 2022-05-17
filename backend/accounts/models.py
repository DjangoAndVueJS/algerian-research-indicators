# For translation purpose
from email.policy import default
from django.utils.translation import gettext_lazy as _
from django.db import models

# For the Custom user
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# to specify a range
# from django.core.validators import MinValueValidator, MaxValueValidator


class ResearcherUserManager(BaseUserManager):
    """
    The Manager of the user(Researcher)
    """

    def create_user(self, first_name, last_name, google_scholar_account, email, password=None, **other_fields):
        """
        Simple user
        """
        if not email:
            raise ValueError(_("the email must be set "))
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name,
                          google_scholar_account=google_scholar_account, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, google_scholar_account, email, password=None, **other_fields):
        """
        Superuser(admin)
        """
        # this kind of code is for testing purpose
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError("Superuser must be is_staff")

        if other_fields.get('is_active') is not True:
            raise ValueError("Superuser must be is_active")

        if other_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must be is_superuser")
        return self.create_user(first_name, last_name, google_scholar_account, email, password, **other_fields)


# custom user
class Researcher(AbstractBaseUser, PermissionsMixin):
    """
    The user profile of a researcher 
    """
    # attributes
    first_name = models.CharField(max_length=150, default='')
    last_name = models.CharField(max_length=150, default='')
    email = models.EmailField(_('email adress'), unique=True)
    speciality = models.CharField(max_length=150, blank=True)
    grade = models.CharField(max_length=200, blank=True)

    # extra info
    #
    image = models.ImageField(blank=True, upload_to='user_pic')
    twitter_account = models.URLField(blank=True)
    linkedin_account = models.URLField(blank=True)
    google_scholar_account = models.URLField(blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    # Relationship between Database tables
    # Location --> Wilaya : A location table
    location_researchers = models.ForeignKey(
        'Location', on_delete=models.SET_NULL, null=True, blank=True
    )
    etablisment_researchers = models.ForeignKey(
        'Etablisment', on_delete=models.SET_NULL, null=True, blank=True)
    division_researchers = models.ForeignKey(
        'Division', on_delete=models.SET_NULL, null=True, blank=True)
    laboratoire_researchers = models.ForeignKey(
        'Laboratoire', on_delete=models.SET_NULL, null=True, blank=True)
    equipe_researchers = models.ForeignKey(
        'Equipe', on_delete=models.SET_NULL, null=True, blank=True)
    directions_researchers = models.ForeignKey(
        'Directions', on_delete=models.SET_NULL, null=True, blank=True)
    # affiliations = models.CharField(max_length=150)

    # interests

    # roles
    # is_team_leader , is_division
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = ResearcherUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'google_scholar_account']

    class Meta:
        ordering = ['date_joined']

    # Researche : YAHIA Ilyes
    def __str__(self) -> str:
        return " ".join(["Researcher :", self.last_name.upper(), self.first_name.capitalize()])

    def get_username(self) -> str:
        return super().get_username()


class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=30)
    # validators=[MinValueValidator(1), MaxValueValidator(58)],

    def __str__(self) -> str:
        return self.state_name


# tutelle --> MESRS

#  Les etablisements de le MESRS (le ministre Abdelbaqi Benziane)
# Établissements publics sous tutelle
 # avec une seule Organisation mère
    # Ministère de l'Enseignement supérieur et de la Recherche scientifique
    # Affiliation
    # Ministère de l'enseignement supérieur et de la recherche scientifique
class Etablisment(models.Model):
    nom = models.CharField(max_length=200, default='')
    logo = models.ImageField(null=True, blank=True)
    # Type

    domaine_activite = models.CharField(max_length=200, blank=True)
    sites_web = models.URLField(blank=True)
    # Relations
    location = models.ForeignKey(
        'Location', on_delete=models.CASCADE, null=True)
    chef_etablisement = models.OneToOneField(
        'Researcher', on_delete=models.SET_NULL, null=True)
    directions = models.ForeignKey(
        'Directions', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nom


class Division(models.Model):
    nom = models.CharField(max_length=200, default='')

    # relationshi
    etablisment = models.ForeignKey(
        'Etablisment', on_delete=models.CASCADE, null=True)
    chef_div = models.OneToOneField(
        'Researcher', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nom


class Laboratoire(models.Model):
    nom = models.CharField(max_length=200)
    # relationship
    division = models.ForeignKey(
        'Division', on_delete=models.CASCADE, null=True)
    chef_labo = models.OneToOneField(
        'Researcher', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nom


class Equipe(models.Model):
    nom = models.CharField(max_length=200)

    # Relationship
    laboratoire = models.ForeignKey(
        'Laboratoire', on_delete=models.CASCADE, null=True)
    chef_equipe = models.OneToOneField(
        'Researcher', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nom


# DGRSD
class Directions(models.Model):
    nom = models.CharField(max_length=150, )
    chef_direction = models.OneToOneField(
        'Researcher', on_delete=models.SET_NULL, null=True)
