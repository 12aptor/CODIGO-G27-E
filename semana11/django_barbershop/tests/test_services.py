import pytest
from rest_framework.test import APIClient
from rest_framework import status
from faker import Faker

fake = Faker()

@pytest.fixture
def client_with_token():
    client = APIClient()
    role_data = {
        'name': 'ADMIN'
    }
    role = client.post('/api/roles/', role_data, format='json')
    assert role.status_code == status.HTTP_201_CREATED

    user_data = {
        'name': fake.name(),
        'email': fake.email(),
        'password': fake.password(length=10),
        'role': role.data['id']
    }
    user = client.post('/api/auth/register/', user_data, format='json')
    assert user.status_code == status.HTTP_201_CREATED

    login_data = {
        'email': user_data['email'],
        'password': user_data['password']
    }
    login = client.post('/api/auth/login/', login_data, format='json')
    assert login.status_code == status.HTTP_200_OK

    client.credentials(HTTP_AUTHORIZATION=f'Bearer {login.data["access"]}')
    return client

@pytest.mark.django_db
def test_list_services(client_with_token):
    services = client_with_token.get('/api/services/')
    assert services.status_code == status.HTTP_200_OK
    assert isinstance(services.data, list)

@pytest.mark.django_db
def test_create_service(client_with_token):
    service_data = {
        'name': 'Test Service',
        'description': 'This is a test service.',
        'price': 20.00,
        'duration': 1
    }
    service = client_with_token.post('/api/services/', service_data, format='json')
    assert service.status_code == status.HTTP_201_CREATED
    assert isinstance(service.data, dict)
    assert isinstance(service.data['id'], int)
    assert service.data['name'] == service_data['name']