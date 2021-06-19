from django.db import models
from food.models import Food
from user.models import CustomUser


class Like(models.Model):
    owner = models.ForeignKey(CustomUser, related_name='likes', on_delete=models.CASCADE)
    food = models.ForeignKey(Food, related_name="likes", on_delete=models.CASCADE)
    likes_number = models.AutoField(primary_key=True)
    like = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.food}-->{self.owner}"

    class Meta:
        unique_together = ('food', 'owner')


class DisLike(models.Model):
    owner = models.OneToOneField(CustomUser, related_name='dis_likes', on_delete=models.CASCADE)
    food = models.ForeignKey(Food, related_name="dis_likes", on_delete=models.CASCADE)
    dislikes_number = models.AutoField(primary_key=True)
    dislike = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.food}-->{self.owner}"

    class Meta:
        unique_together = ('food', 'owner')
