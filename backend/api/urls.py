from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *


router = routers.DefaultRouter()
router.register(r'orders', OrderView)
router.register(r'users', CustomUserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('reg/', UserRegistrationView.as_view(), name='reg'),
    # path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/', LoginView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
