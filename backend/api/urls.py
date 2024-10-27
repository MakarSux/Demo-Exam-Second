from django.urls import path, include

from rest_framework import routers

from .views import OrderView, UserRegistrationView


router = routers.DefaultRouter()
router.register(r'orders', OrderView)


urlpatterns = [
    path('', include(router.urls)),
    path('reg/', UserRegistrationView.as_view(), name='reg'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
