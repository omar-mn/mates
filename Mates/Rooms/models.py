from django.db import models
from Users.models import account

class Room(models.Model):
    
    class CategoryChoices(models.TextChoices):
        STUDY           = 'study'
        GAMES           = 'games'
        PROGRAMMING     = 'programing'
        LIFEISSUES      = 'life issues'
        OTHER           = 'other'

    name                = models.CharField(max_length=50)
    description         = models.TextField(max_length=500 , blank=True , null=True , default="الاخ مكسل يضيف وصف للروم او بيجرب ف مشيها يخوياو اعتبرها عشوائية او حسب الاسم بقا )موفر عليكم وقت الكتابة اهو و بضيف من عندي , عشان انا ديفيلوبر طرش جدا.")
    created_date        = models.DateField(auto_now_add=True)
    user                = models.ManyToManyField(account , through='MemberShip')
    category            = models.CharField(choices=CategoryChoices.choices , default=CategoryChoices.OTHER)


class MemberShip(models.Model):
    user                = models.ForeignKey(account ,on_delete=models.CASCADE)
    room                = models.ForeignKey(Room , on_delete=models.CASCADE)
    joinDate            = models.DateField(auto_now_add=True)