import json

from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import JsonResponse
from django.views import View

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from ads.models import Ad, User, Location, Category
from ads.serializers import AdSerializer, CategorySerializer, LocationSerializer, UserSerializer, UserCreateSerializer, \
    UserUpdateSerializer
from ads_dj import settings


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


"""
    AD
"""


class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def get(self, request, *args, **kwargs):
        cat = request.GET.get('cat')
        text = request.GET.get('text')
        location = request.GET.get('location')
        price_from = request.GET.get('price_from', 0)
        price_to = request.GET.get('price_to', 1000000000)

        if cat:
            self.queryset = self.queryset.filter(category__id__exact=cat)

        if text:
            self.queryset = self.queryset.filter(name__icontains=text)

        if location:
            self.queryset = self.queryset.filter(author__locations__name__icontains=location)

        if price_from or price_to:
            self.queryset = self.queryset.filter(price__range=[price_from, price_to])

        return super().get(request, *args, **kwargs)


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdImageView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


"""
    CATEGORY
"""


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDeleteView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


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


class UserAdDetailView(View):
    def get(self, request):
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
