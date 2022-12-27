import pytest


@pytest.mark.django_db
def test_selection_create_true(client, admin_token):
    data = {
        "name": "Тест-нейм123321",
    }

    expected_response = {
        "id": 1,
        "name": "Тест-нейм123321",
    }

    response = client.post(
        "/selections/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Bearer " + admin_token
    )

    assert response.status_code == 201
    assert response.data == expected_response
