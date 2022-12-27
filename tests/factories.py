import factory.django

from ads.models import Ad


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "Тест-нейм12321321321"
    price = 150
    description = "Тестовое описание 213213121"
    is_published = False
