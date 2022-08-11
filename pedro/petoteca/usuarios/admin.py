from django.contrib import admin
from usuarios.models import Usuario
from django.contrib import admin

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('nome', 'senha', 'email')