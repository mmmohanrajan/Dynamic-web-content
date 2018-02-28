# from django.conf.urls import include, url
from django.urls import path, include
from api.v1.account.views import UserRegister
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from rest_framework.routers import DefaultRouter


from api.v1.hotel.views import HotelViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'hotel', HotelViewSet)

urlpatterns = [
	# The API URLs are now determined automatically by the router.
	path('', include(router.urls)),

    path('account/login/', obtain_jwt_token),
    path('account/token-refresh/', refresh_jwt_token),
    path('account/token-verify/', verify_jwt_token),
    path('account/register/', UserRegister.as_view()),
]