from django.db import models
from food.models import Food
from user.models import CustomUser


class Marks(models.Model):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    choose_your_mark = [
        (one, 'не посоветую никому'),
        (two, 'не очень'),
        (three, 'нормально'),
        (four, 'вкусно'),
        (five, 'Пальчики оближешь!'),
    ]


class Review(models.Model):
    body = models.TextField()
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.food}->{self.body}'


class Mark(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='mark')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    mark = models.SmallIntegerField(choices=Marks.choose_your_mark)

    def __str__(self):
        return f'{self.owner}->{self.food}->{self.mark}'

    class Meta:
        unique_together = ('food',
                           'owner')
