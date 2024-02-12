import pytest
from main import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


@pytest.fixture
def position_fixture():
    return models.Positions.objects.create(name="worker", wage=9.0)


@pytest.fixture
def employee_fixture(position_fixture):
    position = position_fixture
    return models.Employees.objects.create(
        age=19, position=position, name="dummy", surname="dummy2"
    )


@pytest.fixture
def cage_fixture(employee_fixture):
    return models.Cages.objects.create(category="l", caretaker=employee_fixture)


@pytest.fixture
def super_user_fixture():
    return User.objects.create_superuser(username="test", password="test")


@pytest.fixture
def token_fixture(super_user_fixture):
    return Token.objects.create(user=super_user_fixture)
