import pytest
from rest_framework.test import APIClient, force_authenticate
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class TestOverall(APITestCase):
    def test_overall_view(self):
        request = self.client.get("http://127.0.0.1:8000/")
        self.assertEqual(request.status_code, 200)


@pytest.mark.django_db
def test_animals_overall_view_get_and_delete(token_fixture, super_user_fixture):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Token " + token_fixture.key)
    request = client.get("http://127.0.0.1/animals")
    assert request.status_code == 200
    request = client.delete("http://127.0.0.1/animals")
    assert request.status_code == 204


@pytest.mark.django_db
@pytest.mark.parametrize(
    "input,outcome",
    (
        (
            {"kind": "l", "name": "leon", "cage": None, "AdditionalInfo": ""},
            status.HTTP_200_OK,
        ),
        (
            {"kind": "p", "name": "leon", "cage": None, "AdditionalInfo": ""},
            status.HTTP_400_BAD_REQUEST,
        ),
        (
            {"kind": "l", "name": "", "cage": None, "AdditionalInfo": ""},
            status.HTTP_400_BAD_REQUEST,
        ),
    ),
)
def test_animals_overall_view_post(token_fixture, input, outcome, cage_fixture):
    client = APIClient()
    if input["cage"] == None:
        input["cage"] = cage_fixture.pk
    client.credentials(HTTP_AUTHORIZATION="Token " + token_fixture.key)
    request = client.post("http://127.0.0.1:8000/animals", data=input)
    assert request.status_code == outcome


@pytest.mark.django_db
def test_animals_detailed_view(cage_fixture, token_fixture):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Token " + token_fixture.key)
    animal = {
        "kind": "l",
        "name": "leon",
        "cage": cage_fixture.pk,
        "AdditionalInfo": "",
    }
    request = client.get("http://127.0.0.1:8000/animals/1")
    assert request.status_code == 404
    client.post("http://127.0.0.1:8000/animals", data=animal)
    request = client.get("http://127.0.0.1:8000/animals/1")
    assert request.status_code == 200
    request = client.delete("http://127.0.0.1:8000/animals/1")
    assert request.status_code == 204
    request = client.get("http://127.0.0.1:8000/animals/1")
    assert request.status_code == 404


@pytest.mark.django_db
def test_register_view():
    client = APIClient()
    user1 = {"username": "test", "password": "test", "email": "test@gmail.com"}
    request = client.post("http://127.0.0.1/register", data=user1)
    assert request.status_code == status.HTTP_200_OK
    assert User.objects.get(username=user1["username"]).password != user1["password"]
    assert Token.objects.get(user=User.objects.get(username=user1["username"]).pk)
    request = client.post("http://127.0.0.1/register", data=user1)
    assert request.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_login_view():
    client = APIClient()
    user = {"username": "test", "password": "test", "email": "test@gmail.com"}
    client.post("http://127.0.0.1/register", data=user)
    request = client.post(
        "http://127.0.0.1/login",
        data={"username": user["username"], "password": "wrong_password"},
    )
    assert request.status_code == 404
    request = client.post(
        "http://127.0.0.1/login",
        data={"username": "wrong_username", "password": user["password"]},
    )
    assert request.status_code == 404
    request = client.post(
        "http://127.0.0.1/login",
        data={"username": user["username"], "password": user["password"]},
    )
    assert request.status_code == 200
    token = Token.objects.get(user=User.objects.get(username=user["username"]).pk).key
    assert request.data["token"] == token


@pytest.mark.django_db
def test_positions_overall_view_get_and_delete():
    client = APIClient()
    request = client.get("http://127.0.0.1:8000/positions")
    assert request.status_code == 200
    request = client.delete("http://127.0.0.1:8000/positions")
    assert request.status_code == 204


@pytest.mark.django_db
@pytest.mark.parametrize(
    "test_input,outcome",
    (
        ({"wage": 20, "name": "dsfsd"}, status.HTTP_200_OK),
        ({"wage": 5, "name": "dsfsd"}, status.HTTP_400_BAD_REQUEST),
        ({"wage": 20, "name": ""}, status.HTTP_400_BAD_REQUEST),
    ),
)
def test_positions_overall_view_post(test_input, outcome):
    client = APIClient()
    request = client.post("http://127.0.0.1:8000/positions", data=test_input)
    assert request.status_code == outcome


@pytest.mark.django_db
def test_positions_detailed():
    client = APIClient()
    position = {"wage": 20, "name": "dsfsd"}
    client.post("http://127.0.0.1:8000/positions", data=position)
    request = client.get("http://127.0.0.1:8000/positions/1")
    assert request.status_code == 200
    request = client.delete("http://127.0.0.1:8000/positions/1")
    assert request.status_code == 204


@pytest.mark.django_db
def test_cages_overall_view_get_and_delete():
    client = APIClient()
    request = client.get("http://127.0.0.1:8000/cages")
    assert request.status_code == 200
    request = client.delete("http://127.0.0.1:8000/cages")
    assert request.status_code == 204


@pytest.mark.django_db
@pytest.mark.parametrize(
    "test_input,outcome",
    (
        ({"category": "s", "caretaker": None}, status.HTTP_200_OK),
        ({"category": "s", "caretaker": ""}, status.HTTP_200_OK),
    ),
)
def test_cages_overall_view_post(test_input, outcome, employee_fixture):
    client = APIClient()
    if test_input["caretaker"] == None:
        test_input["caretaker"] = employee_fixture.pk
    request = client.post("http://127.0.0.1:8000/cages", data=test_input)
    assert request.status_code == outcome


@pytest.mark.django_db
def test_cages_detailed(employee_fixture):
    client = APIClient()
    cage = {"category": "s", "caretaker": employee_fixture.pk}
    client.post("http://127.0.0.1:8000/cages", data=cage)
    request = client.get("http://127.0.0.1:8000/cages/1")
    assert request.status_code == 200
    request = client.delete("http://127.0.0.1:8000/cages/1")
    assert request.status_code == 204
