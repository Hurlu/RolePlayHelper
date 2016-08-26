from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField
# Create your models here.


class SkillStep(models.Model):
    bonus = models.TextField(_('Boon'))
    needed_exp = models.IntegerField(_('Needed exp'))
    number = models.IntegerField(_('Step number'))

    def __str__(self):
        return 'Step {}'.format(self.number)


class SkillGrid(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()
    primary_effect_cases = models.CharField(max_length=500)
    secondary_effect_cases = models.CharField(max_length=500)

    def __str__(self):
        return 'Skill grid'


class Skill(models.Model):
    name = models.CharField(_('Name'), max_length=30)
    cost = models.IntegerField(_('Cost'))
    flavor_text = models.TextField(_('Flavor text'))
    steps = models.ManyToManyField(SkillStep, verbose_name=_('Steps'))
    grid = models.ForeignKey(SkillGrid, verbose_name=_('Skill grid'))

    def __str__(self):
        return self.name


class SkillInstance(models.Model):
    skill = models.ForeignKey(Skill)
    xp = models.IntegerField(_('Xp'), default=0)
    playerskill = models.ForeignKey('PlayerSkills')


class PlayerSkills(models.Model):
    skills = models.ManyToManyField(Skill, verbose_name=_('Skills'),
                                    blank=True, through=SkillInstance)

    def __str__(self):
        try:
            return self.player.first_name + '\'s Skills'
        except:
            return 'Anonymous skillsheet :,('


class ItemType(models.Model):
    name = models.CharField(_('Name'), max_length=100)

    def __str__(self):
        return self.name


class ItemCase(models.Model):
    pos_x = models.IntegerField(_('Pos X'))
    pos_y = models.IntegerField(_('Pos Y'))
    pic = FilerImageField(verbose_name=_('Picture'))

    def __str__(self):
        return 'Case [{}, {}]'.format(self.pos_x, self.pos_y)


class ItemGrid(models.Model):
    width = models.IntegerField(_('Width'))
    height = models.IntegerField(_('Height'))
    origin_case = models.OneToOneField(ItemCase, verbose_name=_('Origin case'), related_name=_('origin'))
    cases = models.ManyToManyField(ItemCase, verbose_name=_('Cases'),
                                   blank=True, limit_choices_to={'itemgrid__id': id(object)})

    def __str__(self):
        return 'Item grid'
    

class Item(models.Model):
    name = models.CharField(_('Name'), max_length=67)
    flavor_text = models.TextField(_('Flavor text'))
    itemgrid = models.ForeignKey(ItemGrid)

    def __str__(self):
        return self.name


class SingleItem(models.Model):
    items = models.ForeignKey(Item, verbose_name=_('Items'))
    inventory = models.ForeignKey('Inventory')
    quantity = models.IntegerField(_('Quantity'), default=1)
    origin_position_x = models.IntegerField(_('Pos X'))
    origin_position_y = models.IntegerField(_('Pos Y'))

    def __str__(self):
        return 'Quantity'


class Inventory(models.Model):
    items = models.ManyToManyField(Item, verbose_name=_('Items'), through=SingleItem,
                                   related_name=_('invent_item'), blank=True)

    def __str__(self):
        try:
            return self.player.first_name + '\'s inventory'
        except:
            return 'Anonymous inventory :,('


class Boon(models.Model):
    name = models.CharField(_('Name'), max_length=40)
    flavor_text = models.TextField(_('Flavor text'))
    picture = FilerImageField()

    def __str__(self):
        return self.name


class DefensiveEquipment(Item):
    type = models.ForeignKey(ItemType, verbose_name=_('Type'), related_name=_('armortype'))
    defensive_value = models.IntegerField(_('Defensive value'))
    boon_value = models.IntegerField(_('Boon value'))
    boon = models.ManyToManyField(Boon, verbose_name=_('Boon'), related_name=_('armorboon'), blank=True)


class OffensiveEquipment(Item):
    type = models.ForeignKey(ItemType, related_name=_('Type'))
    defensive_value = models.IntegerField(_('Defensive value'))
    attack_value = models.IntegerField(_('Attack value'))
    boon_value = models.IntegerField(_('Boon value'))
    boon = models.ManyToManyField(Boon, verbose_name=_('Boon'), related_name=_('weaponboon'), blank=True)
    skills = models.ManyToManyField(Skill, verbose_name=_('Skills'), related_name=_('weaponskill'),
                                    blank=True)


class Equipment(models.Model):
    weapon = models.ForeignKey(OffensiveEquipment, verbose_name=_('Weapon'), related_name=_('Weapon'), blank=True, null=True)
    head = models.ForeignKey(DefensiveEquipment, limit_choices_to={'type__name': 'head'}, verbose_name=_('Head'),
                             related_name=_('head'), blank=True, null=True)
    torso = models.ForeignKey(DefensiveEquipment, limit_choices_to={'type__name': 'torso'}, verbose_name=_('Torso'),
                              related_name=_('torso'), blank=True, null=True)
    left_arm = models.ForeignKey(DefensiveEquipment, limit_choices_to={'type__name': 'left_arm'},
                                 verbose_name=_('Left arm'), related_name=_('left_arm'), blank=True, null=True)
    left_leg = models.ForeignKey(DefensiveEquipment, limit_choices_to={'type__name': 'left_leg'},
                                 verbose_name=_('Left leg'), related_name=_('left_leg'), blank=True, null=True)
    right_arm = models.ForeignKey(DefensiveEquipment, limit_choices_to={'type__name': 'right_arm'},
                                  verbose_name=_('Right arm'), related_name=_('right_arm'), blank=True, null=True)
    right_leg = models.ForeignKey(DefensiveEquipment, limit_choices_to={'type__name': 'right_leg'},
                                  verbose_name=_('Right leg'), related_name=_('right_leg'), blank=True, null=True)

    def __str__(self):
        try:
            return self.player.first_name + '\'s Equipment'
        except:
            return 'Anonymous equipment :,('


class LifeStatus(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    flavor_text = models.TextField(_('Flavor text'))
    picture = FilerImageField()

    def __str__(self):
        return self.name


class Status(models.Model):
    life_head = models.IntegerField(_('Head\'s HP'), default=100)
    life_left_arm = models.IntegerField(_('Left arm\'s HP'), default=100)
    life_right_arm = models.IntegerField(_('Right arm\'s HP'), default=100)
    life_left_leg = models.IntegerField(_('Left leg\'s HP'), default=100)
    life_right_leg = models.IntegerField(_('Right leg\'s HP'), default=100)
    life_status = models.ManyToManyField(LifeStatus, verbose_name=_('Life status'), blank=True)

    def __str__(self):
        try:
            return self.player.first_name + '\'s Status'
        except:
            return 'Anonymous status :,('


class Stats(models.Model):
    strength = models.IntegerField(_('Strength'))
    dexterity = models.IntegerField(_('Dexterity'))
    intelligence = models.IntegerField(_('Intelligence'))
    eloquence = models.IntegerField(_('Eloquence'))
    instinct = models.IntegerField(_('Instinct'))
    craftiness = models.IntegerField(_('Craftiness'))
    
    def __str__(self):
        try:
            return self.player.first_name + '\'s Stats'
        except:
            return 'Anonymous stats :,('



class Player(models.Model):
    first_name = models.CharField(_('First name'), max_length=30)
    last_name = models.CharField(_('Last name'), max_length=30)
    nickname = models.CharField(_('Nickname'), max_length=30)
    skills = models.OneToOneField(PlayerSkills, verbose_name=_('Skills'), blank=True, related_name='player')
    inventory = models.OneToOneField(Inventory, verbose_name=_('Inventory'), related_name='player')
    equipment = models.OneToOneField(Equipment, verbose_name=_('Equipment'), related_name='player')
    status = models.OneToOneField(Status, verbose_name=_('Status'), related_name='player')
    stats = models.OneToOneField(Stats, verbose_name=_('Stats'), related_name='player')
    
    def __str__(self):
        return "{} \'{}\' {}".format(self.first_name, self.nickname, self.last_name)
