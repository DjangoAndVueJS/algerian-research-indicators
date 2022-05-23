from enum import unique
from re import U
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
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

    def create_user(self, first_name, last_name, speciality, grade, google_scholar_account, email, password=None, **other_fields):
        """
        Simple user
        """
        if not email:
            raise ValueError(_("the email must be set "))
        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name, speciality=speciality, grade=grade,
                          google_scholar_account=google_scholar_account, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, speciality, grade, google_scholar_account, email, password=None, **other_fields):
        """
        Superuser(admin)
        """
        # this kind of code is for testing purpose
        user = self.create_user(
            first_name, last_name, speciality, grade, google_scholar_account, email, password, **other_fields,)
        user.is_admin = True
        user.save(using=self._db)
        return user


# custom user
class Researcher(AbstractBaseUser, PermissionsMixin):
    """
    The user profile of a researcher 
    """
    # attributes
    email = models.EmailField(_('email adress'), unique=True)
    first_name = models.CharField(max_length=150, default='')
    last_name = models.CharField(max_length=150, default='')
    speciality = models.CharField(max_length=150, blank=False)
    grade = models.CharField(max_length=200, blank=False)
    google_scholar_account = models.URLField(blank=True, unique=True)

    # extra info
    image = models.ImageField(blank=True, upload_to='user_pic')
    linkedin_account = models.URLField(blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    # Relationship between Database tables
    equipe_researchers = models.ForeignKey(
        'Equipe', on_delete=models.SET_NULL, null=True, blank=True)
    # Role dans l'organissme
    # affecte = models.BooleanField(default=False)
    # roleD = (('Membre d\'equipe ', 'Membre d\'equipe '),
    #          ('Chef d\'equipe', 'Chef d\'equipe'),
    #          ('Chef de Laboratoire', 'Chef de Laboratoire'),
    #          ('Chef de Divsion', 'Chef de Division'),
    #          ('Chef d\'etablisment', 'Chef d\'etablisment'))
    # role = models.CharField(max_length=100, null=True, choices=roleD)
    """
    user roles can be diffrente
        1 -> mesrs == admin 
        2 -> dgrst == 
        3 -> chef_lab 
        4 -> chef_div 
        5 -> chef_eta
        6 -> chef_equipe
    """
    # interests
    is_active = models.BooleanField(default=True)
    # is_admin = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = ResearcherUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',
                       'speciality', 'grade', 'google_scholar_account']

    class Meta:
        ordering = ['-date_joined']

    # def clean(self):
    #     if self.google_scholar_account[0:42] != 'https://scholar.google.com/citations?user=':
    #         raise ValidationError('format compte google scholar non valide')

    def __str__(self) -> str:
        return " ".join(["Researcher :", self.first_name.upper(), self.last_name.capitalize()])

    def get_username(self) -> str:
        return super().get_username()

    # def has_perm(self, perm: str, obj: Optional[_AnyUser] = ...) -> bool:
    #     return super().has_perm(perm, obj)

    def get_google_scholar_id(self):
        return self.google_scholar_account.partition('user=')[2][:12]

    def has_perm(self, perm, obj=None) -> bool:
        return True

    def has_module_perms(self, app_label) -> bool:
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Equipe(models.Model):
    # uuid id for every teams
    nom = models.CharField(max_length=200)
    site_web = models.URLField(blank=True)
    # Relationship
    laboratoire = models.ForeignKey(
        'Laboratoire', on_delete=models.CASCADE, null=True)
    chef_equipe = models.OneToOneField(
        'Researcher', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        permissions = [
            ("add_team", "Can add team"),
            ("delete_team", "Can delete team"),
            ("change_team", "Can change team .... ")
        ]


class Location(models.Model):
    id = models.IntegerField(primary_key=True,)
    state_name = models.CharField(max_length=30, blank=False)
    # validators=[MinValueValidator(1), MaxValueValidator(58)],

    def __str__(self) -> str:
        return self.state_name


class Etablisment(models.Model):
    nom = models.CharField(max_length=200, default='')
    logo = models.ImageField(null=True, blank=True)
    site_web = models.URLField(blank=True)
    location = models.ForeignKey(
        'Location', on_delete=models.CASCADE, null=True)
    chef_etablisement = models.OneToOneField(
        'Researcher', on_delete=models.SET_NULL, null=True, blank=True)
    # directions = models.ForeignKey(
    #     'Directions', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nom


class Division(models.Model):
    nom = models.CharField(max_length=200, default='')
    site_web = models.URLField(blank=True)

    # relationshi
    etablisment = models.ForeignKey(
        'Etablisment', on_delete=models.CASCADE, null=True)
    chef_div = models.OneToOneField(
        'Researcher', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nom


class Laboratoire(models.Model):
    nom = models.CharField(max_length=200)
    site_web = models.URLField(blank=True)

    # relationship
    division = models.ForeignKey(
        'Division', on_delete=models.CASCADE, null=True)
    chef_labo = models.OneToOneField(
        'Researcher', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nom


class Directions(models.Model):
    nom = models.CharField(max_length=150, )
    chef_direction = models.OneToOneField(
        'Researcher', on_delete=models.SET_NULL, null=True)
