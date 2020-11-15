from django.conf import settings
from django.db import models
from django.utils import timezone


class Ingridient(models.Model):
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    price_hundred_gramms = models.IntegerField()
    calorie = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()
    carbohydrates = models.IntegerField()



    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.title




class Dish(models.Model):
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    cost = models.IntegerField()

    def __str__(self):
        return self.title


class IngridientOfDish(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='dish')
    ingridient = models.ForeignKey(Ingridient, on_delete=models.CASCADE, related_name='ingridient')
    created_date = models.DateTimeField(default=timezone.now)
    weight = models.IntegerField()
