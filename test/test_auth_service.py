import pytest
from dtos.auth_dtos import LoginRequestDTO, RegisterRequestDTO, RegisterResponseDTO
from exceptions.erros import UserAlreadyExistsError
from models.user import User
from services.auth_service import autenticate_user, create_user


REGISTER_USER_DATA = RegisterRequestDTO(
    email='teste@teste.com', full_name='Teste', password='senha123'
)

LOGIN_USER_DATA = LoginRequestDTO(
    email='teste@teste.com', password='senha123'
)


@pytest.fixture
def mocked_user():
    u = User(email='teste@teste.com', full_name='Teste')
    u.set_password(password='senha123')
    yield u


def test_create_user_success_return(mocker):  
    mocker.patch(
        'services.auth_service.save_user',
        return_value=None)
    result = create_user(REGISTER_USER_DATA)    
    assert type(result) == RegisterResponseDTO


def test_create_user_failure_return(mocker):
    with pytest.raises(UserAlreadyExistsError) as e:
        mocker.patch(
            'services.auth_service.save_user',
            side_effect=UserAlreadyExistsError)
        result = create_user(REGISTER_USER_DATA)
        assert type(e) == UserAlreadyExistsError
    

def test_autenticate_user_success(mocker, mocked_user):
    expected_result = 'token'
    mocker.patch(
        'services.auth_service.get_by_email',
        return_value=mocked_user)
    mocker.patch(
        'services.auth_service.create_access_token',
        return_value=expected_result)

    
    result = autenticate_user(LOGIN_USER_DATA)
    assert result == expected_result
    

def test_autenticate_user_email_not_found(mocker):
    mocker.patch(
        'services.auth_service.get_by_email',
        return_value=None)
    result = autenticate_user(LOGIN_USER_DATA)
    assert result is None


def test_autenticate_user_wrong_password(mocker, mocked_user):
    mocker.patch(
        'services.auth_service.get_by_email',
        return_value=mocked_user)
    login_data = LoginRequestDTO(LOGIN_USER_DATA.email, 'wrong_password')
    result = autenticate_user(login_data)
    assert result is None
