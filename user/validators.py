from datetime import date

from rest_framework import serializers


class BirthDayValidator:
    def __init__(self, base_age: int):
        self.base_age = base_age

    def __call__(self, value: date):
        user_age = (date.today() - value).days // 365.2425

        if user_age < self.base_age:
            raise serializers.ValidationError(f'Регистрация пользователя младше {self.base_age} лет запрещена!')


class EmailValidator:
    def __init__(self, banned_domains: tuple):
        self.banned_domains = banned_domains

    def __call__(self, value: str):
        domain = value.split('@')[1]

        if domain in self.banned_domains:
            raise serializers.ValidationError('Домен запрещен!')
