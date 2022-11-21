from rest_framework import serializers

from ads.models import Ad, Location, Category, User


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


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(read_only=True, many=True, slug_field='name')

    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        many=True,
        queryset=Location.objects.all(),
        slug_field='name',
        required=False,
    )

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, *, raise_exception=False):
        self.initial_data = self.initial_data.copy()
        self._locations = self.initial_data.pop('locations')
        res = super().is_valid(raise_exception=raise_exception)
        self.initial_data.update({'locations': self._locations})

        return res

    def create(self, validated_data):
        validated_data.pop('locations')
        user = User.objects.create(**validated_data)

        for location in self._locations:
            location_object, _ = Location.objects.get_or_create(name=location)
            user.locations.add(location_object)

        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        required=False,
        many=True,
        slug_field='name',
        queryset=Location.objects.all()
    )

    class Meta:
        model = User
        fields = "__all__"

    def is_valid(self, *, raise_exception=False):
        self.initial_data = self.initial_data.copy()
        self._locations = self.initial_data.pop('locations')
        res = super().is_valid(raise_exception=raise_exception)
        self.initial_data.update({'locations': self._locations})

        return res

    def save(self):
        user = super().save()

        for location in self._locations:
            location_object, _ = Location.objects.get_or_create(name=location)
            user.locations.add(location_object)

        user.save()
        return user
