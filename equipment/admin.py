from django.contrib import admin
from .models import *
# Register your models here.

class ItemTypeAdmin(admin.ModelAdmin):
    pass


class ItemAdmin(admin.ModelAdmin):
    pass


class InventoryAdmin(admin.ModelAdmin):
    pass


class EquipmentAdmin(admin.ModelAdmin):
    pass


class PlayerAdmin(admin.ModelAdmin):
    pass


admin.site.register(ItemType, ItemTypeAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Player, PlayerAdmin)
