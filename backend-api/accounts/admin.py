from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from accounts import models


class UserCreationForm(forms.ModelForm):
    """
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = models.Researcher
        fields = ('email', 'first_name', 'last_name', 'speciality',
                  'grade', 'google_scholar_account')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("passwords don't match ")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = models.Researcher
        fields = ('email', 'first_name', 'last_name',
                  'speciality', 'grade', 'google_scholar_account', 'is_active', 'is_admin')


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'first_name', 'is_admin', 'last_name', 'speciality',
                    'grade', 'linkedin_account', 'google_scholar_account', 'equipe_researchers')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'speciality',
                                      'grade', 'linkedin_account', 'google_scholar_account',)}),
        ('Permissions', {
         'fields': ('is_admin', 'is_active', 'is_superuser',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'speciality', 'grade', 'linkedin_account', 'google_scholar_account', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Register your models here.
admin.site.register(models.Researcher, UserAdmin)
admin.site.register(models.Location)
admin.site.register(models.Etablisment)
admin.site.register(models.Division)
admin.site.register(models.Laboratoire)
admin.site.register(models.Equipe)
admin.site.register(models.Directions)
