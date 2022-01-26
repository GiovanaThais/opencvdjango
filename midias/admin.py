from django.contrib import admin
from .models import Midias

#registrando model no django admin
@admin.register(Midias)
class MidiasAdmin(admin.ModelAdmin):
    list_display = ('information', 'image', 'action', 'created')
