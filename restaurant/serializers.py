from rest_framework import serializers

class DishSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    cost = serializers.IntegerField()

    def create(self, validated_data):
        return Dish.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.save()
        return instance