from django.contrib import admin
from .models import Ingridient
from .models import Dish
from .models import IngridientOfDish


admin.site.register(Ingridient)
admin.site.register(Dish)
admin.site.register(IngridientOfDish)