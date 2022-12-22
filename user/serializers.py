from rest_framework import serializers

from user.models import User, Location


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
        self._locations = self.initial_data.pop('locations', [])

        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(user.password)

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
        self._locations = self.initial_data.pop('locations', [])

        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()

        for location in self._locations:
            location_object, _ = Location.objects.get_or_create(name=location)
            user.locations.add(location_object)

        user.save()
        return user
