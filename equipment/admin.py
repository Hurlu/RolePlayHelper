from django.contrib import admin
from django_select2.forms import Select2MultipleWidget
from django_select2.forms import Select2Widget
from .models import *
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
# Register your models here.



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


class ItemInline(admin.StackedInline):
    model = SingleItem
    extra = 0


class InventoryAdmin(admin.ModelAdmin):
    inlines = (ItemInline,)


class EquipmentAdmin(admin.ModelAdmin):
    pass


class PlayerForm(ModelForm):
    class Meta:
        widgets = {
            'skills': Select2MultipleWidget(),
        }


class PlayerAdmin(admin.ModelAdmin):
    form = PlayerForm


class StatusAdmin(admin.ModelAdmin):
    pass


class LifeStatusAdmin(admin.ModelAdmin):
    pass


class SkillStepAdmin(admin.ModelAdmin):
    pass


class SkillGridAdmin(admin.ModelAdmin):
    change_form_template = 'admin/equipment/skillgrid/change_form.html'
    suit_form_includes = ('')


class SkillAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('General'), {
            'fields': ('name', 'cost', 'flavor_text', 'steps'),
            'classes': ('suit-tab', 'suit-tab-general',)
        }),
        (_('Skill Grid'), {
            'fields': ('grid', ),
            'classes': ('suit-tab', 'suit-tab-grid',)
        })
    )

    suit_form_tabs = (('general', (_('General'))), ('grid', _('Skillgrid')))


class BoonAdmin(admin.ModelAdmin):
    pass


class SkillsInline(admin.TabularInline):
    extra = 1
    model = SkillInstance

class PlayerSkillsAdmin(admin.ModelAdmin):
    inlines = (SkillsInline,)


class SkillInstanceAdmin(admin.ModelAdmin):
    pass


admin.site.register(SkillInstance, SkillInstanceAdmin)
admin.site.register(PlayerSkills, PlayerSkillsAdmin)
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
