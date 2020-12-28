from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Ingridient, Dish, IngridientOfDish
from datetime import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from .serializers import DishSerializer


class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ['title', 'cost']

def login(request):
    return render(request, 'restaurant/login.html')
@login_required
def home(request):
    return render(request, 'restaurant/home.html')


def dish_list(request):
    dishes = Dish.objects.all()
    # dishes = Dish.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'restaurant/dish_list.html', {'dishes': dishes})

def dish_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, 'restaurant/dish_detail.html', {'dish': dish})

def dish_create(request, template_name='restaurant/dish_form.html'):
    form = DishForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dish_list')
    return render(request, template_name, {'form':form})

def dish_update(request, pk, template_name='restaurant/dish_form.html'):
    dish = get_object_or_404(Dish, pk=pk)
    form = DishForm(request.POST or None, instance=dish)
    if form.is_valid():
        form.save()
        return redirect('dish_list')
    return render(request, template_name, {'form':form})

def dish_delete(request, pk, template_name='restaurant/dish_confirm_delete.html'):
    dish = get_object_or_404(Dish, pk=pk)    
    if request.method=='POST':
        dish.delete()
        return redirect('dish_list')
    return render(request, template_name, {'object':book})

class DishView(APIView):
    def get(self, request):
        dishes = Dish.objects.all()
        serializer = DishSerializer(dishes, many=True)
        return Response({"dishes": serializer.data})

    def post(self, request):
        dish = request.data.get('dish')
        # Create an article from the above data
        serializer = ArticleSerializer(data=dish)
        if serializer.is_valid(raise_exception=True):
            dish_saved = serializer.save()
        return Response({"success": "Dish '{}' created successfully".format(dish_saved.title)})


    def put(self, request, pk):
        saved_dish = get_object_or_404(Dish.objects.all(), pk=pk)
        data = request.data.get('dish')
        serializer = DishSerializer(instance=saved_dish, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            dish_saved = serializer.save()
        return Response({
            "success": "Dish '{}' updated successfully".format(dish_saved.title)
        })

    def delete(self, request, pk):
        # Get object with this pk
        dish = get_object_or_404(Dish.objects.all(), pk=pk)
        dish.delete()
        return Response({
            "message": "Dish with id `{}` has been deleted.".format(pk)
        }, status=204)
