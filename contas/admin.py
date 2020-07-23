from django.contrib import admin

# Register your models here.
from contas.models import Categoria
from contas.models import Transacao


admin.site.register(Categoria)
admin.site.register(Transacao)
