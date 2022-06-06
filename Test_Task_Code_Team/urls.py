from django.urls import path, include

urlpatterns = [
    path('api/v1/foods', include('restaurant_api.urls')),
]
