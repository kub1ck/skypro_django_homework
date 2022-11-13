import json

from django.http import JsonResponse, Http404
from django.views import View
from django.views.generic import DetailView

from ads.models import Ad, Category


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


class AdView(View):
    def get(self, request):
        data = Ad.objects.all()

        response = []

        for ad in data:
            response.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
                "description": ad.description,
                "address": ad.address,
                "is_published": ad.is_published
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        data = json.loads(request.body)

        ad = Ad.objects.create(
            name=data['name'],
            author=data['author'],
            description=data['description'],
            price=data['price'],
            address=data['address'],
            is_published=data['is_published']
        )

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published
        })


class CategoryView(View):
    def get(self, request):
        data = Category.objects.all()

        response = []

        for category in data:
            response.append({
                "id": category.id,
                "name": category.name
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        data = json.loads(request.body)

        category = Category.objects.create(
            name=data['name'],
        )

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        try:
            ad = self.get_object()
        except Http404:
            return JsonResponse({'Error': 'Not found'}, status=404)

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published
        })


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwars):
        try:
            category = self.get_object()
        except Http404:
            return JsonResponse({'Error': 'Not found'}, status=404)

        return JsonResponse({
            "id": category.id,
            "name": category.name
        })
