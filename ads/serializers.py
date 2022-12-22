from rest_framework import serializers

from ads.models import Ad, Category, Selection


class AdSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')
    category = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Ad
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SelectionSerializer(serializers.ModelSerializer):
    items = serializers.SlugRelatedField(read_only=True, slug_field='id')
    owner = AdSerializer(many=True)

    class Meta:
        model = Selection
        fields = '__all__'
