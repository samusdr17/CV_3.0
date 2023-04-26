from django.contrib import admin
from .models import Formacion

# Register your models here.

class FormacionAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Formacion, FormacionAdmin)