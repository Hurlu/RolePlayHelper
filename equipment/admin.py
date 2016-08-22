from django.contrib import admin
from .models import *
# Register your models here.


class SkillGridAdmin(admin.ModelAdmin):
    pass


class ItemCaseAdmin(admin.ModelAdmin):
    pass


class ItemGridAdmin(admin.ModelAdmin):
    pass


class ItemTypeAdmin(admin.ModelAdmin):
    pass


class DefensiveEquipmentAdmin(admin.ModelAdmin):
    pass


class OffensiveEquipmentAdmin(admin.ModelAdmin):
    pass


class StatsAdmin(admin.ModelAdmin):
    pass


class ItemAdmin(admin.ModelAdmin):
    pass


class InventoryAdmin(admin.ModelAdmin):
    pass


class EquipmentAdmin(admin.ModelAdmin):
    pass


class PlayerAdmin(admin.ModelAdmin):
    pass


class StatusAdmin(admin.ModelAdmin):
    pass


class LifeStatusAdmin(admin.ModelAdmin):
    pass


class SkillStepAdmin(admin.ModelAdmin):
    pass


class SkillAdmin(admin.ModelAdmin):
    pass


class BoonAdmin(admin.ModelAdmin):
    pass


admin.site.register(SkillStep, SkillStepAdmin)
admin.site.register(SkillGrid, SkillGridAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(ItemCase, ItemCaseAdmin)
admin.site.register(ItemGrid, ItemGridAdmin)
admin.site.register(ItemType, ItemTypeAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Boon, BoonAdmin)
admin.site.register(DefensiveEquipment, DefensiveEquipmentAdmin)
admin.site.register(OffensiveEquipment, OffensiveEquipmentAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(LifeStatus, LifeStatusAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Stats, StatsAdmin)
admin.site.register(Player, PlayerAdmin)
