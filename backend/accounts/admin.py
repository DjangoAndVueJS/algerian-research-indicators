from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Researcher)
admin.site.register(models.Location)
admin.site.register(models.Etablisment)
admin.site.register(models.Division)
admin.site.register(models.Laboratoire)
admin.site.register(models.Equipe)
admin.site.register(models.Directions)
