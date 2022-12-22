from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import JsonResponse
from django.views import View

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from ads_dj import settings

from user.models import User, Location
from user.serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer, LocationSerializer


"""
    LOCATION
"""


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


"""
    USER
"""


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def user_ad_detail_view(request):
    user_qs = User.objects\
        .prefetch_related("locations")\
        .annotate(total_ads=Count('ad', filter=Q(ad__is_published=True)))

    paginator = Paginator(user_qs, settings.TOTAL_ON_PAGE)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    users = []

    for user in page_obj:
        users.append({
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": user.role,
            "age": user.age,
            "location": list(map(str, user.locations.all())),
            "total_ads": user.total_ads
        })

    response = {
        "items": users,
        "total": paginator.count,
        "num_pages": paginator.num_pages
    }

    return JsonResponse(response, safe=False)
