from django.urls import path, include

from rest_framework import routers

from .views import OrderView, UserRegistrationView, get_csrf_token


router = routers.DefaultRouter()
router.register(r'orders', OrderView)


urlpatterns = [
    path('', include(router.urls)),
    path('get-csrf-token/', get_csrf_token, name='get_csrf_token'),
    path('reg/', UserRegistrationView.as_view(), name='reg'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
