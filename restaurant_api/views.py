from django.db.models import Prefetch
from rest_framework.generics import ListCreateAPIView

from .models import FoodCategory, Food
from .serializers import FoodListSerializer


class FoodAPIView(ListCreateAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        foods = FoodCategory.objects.filter(food__is_publish=True).prefetch_related(
            Prefetch("food", queryset=Food.objects.filter(is_publish=True)))
        return foods.distinct()
