from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class ItemType(models.Model):
    name = models.CharField(max_length=100)

class Item(models.Model):
    name = models.CharField(max_length=67)
    type = models.ForeignKey(ItemType)
    rarity = models.IntegerField()

class Inventory(models.Model):
    items = models.ForeignKey(Item)

class Equipment(models.Model):
    headgear = models.ForeignKey(Item, related_name=_("Headgear"))
    left_arm = models.ForeignKey(Item, related_name=_("Left arm"))
    left_leg = models.ForeignKey(Item, related_name=_("Left leg"))
    right_arm = models.ForeignKey(Item, related_name=_("Right arm"))
    right_leg = models.ForeignKey(Item, related_name=_("Right leg"))

class LifeStatus(models.Model):
    name = models.CharField(max_length=50)

class Status(models.Model):
    life_head = models.IntegerField(default=100)
    life_left_arm = models.IntegerField(default=100)
    life_right_arm = models.IntegerField(default=100)
    life_left_leg = models.IntegerField(default=100)
    life_right_leg = models.IntegerField(default=100)
    life_status =  models.ForeignKey(LifeStatus)

class Player(models.Model):
    first_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    inventory = models.OneToOneField(Inventory)
    equipment = models.OneToOneField(Equipment)
    status = models.OneToOneField(Status)

    def __str__(self):
        return("{} \'{}\' {}".format(self.first_name, self.nickname, self.surname))


