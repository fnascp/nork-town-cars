import pytest

def test_register(mocker, client):
    mocker.patch(
        'services.auth_service.save_user',
        return_value=None
    )

    response = client.post('/register', json={
        "full_name": "Teste User",
        "email": "fabio5@example.com.br",
        "password": "somePassword"
    })

    assert 'id' in response.json


                           
