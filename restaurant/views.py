from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Ingridient, Dish, IngridientOfDish

from .serializers import DishSerializer


def dish_list(request):
    dishes = Dish.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'restaurant/dish_list.html', {'dishes': dishes})


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
