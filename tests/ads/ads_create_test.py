import pytest


@pytest.mark.django_db
def test_ads_create_true(client, admin_token):
    data = {
        "name": "Тест-нейм123321",
        "price": 150,
        "description": "Тестовое описание",
        "is_published": False
    }

    expected_response = {
        "id": 1,
        "author": None,
        "category": None,
        "name": "Тест-нейм123321",
        "price": 150,
        "description": "Тестовое описание",
        "is_published": False,
        "image": None
    }

    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json'
    )

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_ads_create_false(client, admin_token):
    data = {
        "name": "Тест-нейм1233121",
        "price": -150,
        "description": "Тестовое описание",
        "is_published": False
    }

    expected_response = {
        "price": [
            "Ensure this value is greater than or equal to 0."
        ]
    }

    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.data == expected_response
