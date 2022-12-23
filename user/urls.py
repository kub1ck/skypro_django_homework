from django.urls import path

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user.views import LocationViewSet, UserListView, UserCreateView, UserDetailView, UserUpdateView, UserDeleteView, \
    user_ad_detail_view

router = routers.SimpleRouter()
router.register('location', LocationViewSet)

urlpatterns = [
    path('user/', UserListView.as_view()),
    path('user/create/', UserCreateView.as_view()),
    path('user/<int:pk>/', UserDetailView.as_view()),
    path('user/<int:pk>/update/', UserUpdateView.as_view()),
    path('user/<int:pk>/delete/', UserDeleteView.as_view()),

    path('user/Z', user_ad_detail_view),

    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]

urlpatterns += router.urls
