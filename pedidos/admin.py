from django.contrib import admin

from .models import Pedido, LineaPedido
# Register your models here.

class PedidoAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class LineaPedidoAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(LineaPedido)
admin.site.register(Pedido)
