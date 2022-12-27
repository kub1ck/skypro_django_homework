import pytest


@pytest.mark.django_db
def test_retrieve_ad(client, ad, admin_token):
    expected_response = {
        "id": ad.pk,
        "author": None,
        "category": None,
        "name": "Тест-нейм12321321321",
        "price": 150,
        "description": "Тестовое описание 213213121",
        "is_published": False,
        "image": None
    }

    response = client.get(
        f"/ad/{ad.pk}/",
        HTTP_AUTHORIZATION="Bearer " + admin_token
    )

    assert response.status_code == 200
    assert response.data == expected_response
