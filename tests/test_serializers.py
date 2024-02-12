import pytest
from main import serializers


@pytest.mark.parametrize(
    "test_input,expected_outcome",
    (
        ({"name": "worker", "wage": 7.0}, False),
        ({"name": "worker1", "wage": 8.0}, True),
    ),
)
def test_position_serializer(test_input, expected_outcome):
    ser = serializers.PositionsSerializer(data=test_input)
    assert ser.is_valid() == expected_outcome


@pytest.mark.django_db
@pytest.mark.parametrize(
    "test_input,expected_outcome",
    (
        ({"username": "login", "password": "12345", "email": "123@gmail.com"}, True),
        ({"username": "login", "password": "12345", "email": "123@gmail.com"}, True),
    ),
)
def test_register_serializer(test_input, expected_outcome):
    ser = serializers.UserRegisterSerializer(data=test_input)
    assert ser.is_valid() == expected_outcome


@pytest.mark.django_db
@pytest.mark.parametrize(
    "test_input,expected_outcome",
    (
        (
            {
                "username": "login",
                "password": "12345",
            },
            True,
        ),
        (
            {
                "username": "login",
                "password": "12345",
            },
            True,
        ),
    ),
)
def test_login_serializer(test_input, expected_outcome):
    ser = serializers.UserLoginSerializer(data=test_input)
    assert ser.is_valid() == expected_outcome


@pytest.mark.django_db
@pytest.mark.parametrize(
    "test_input,expected_outcome",
    (
        ({"age": 19, "position": None, "name": "david", "surname": "jones"}, True),
        ({"age": 17, "position": None, "name": "david", "surname": "jones"}, False),
        ({"age": 19, "position": None, "name": None, "surname": "jones"}, False),
        ({"age": 19, "position": None, "name": "David", "surname": None}, False),
        ({"age": None, "position": None, "name": "David", "surname": "jones"}, False),
        (
            {"age": 19, "position": None, "name": "special_case", "surname": "jones"},
            True,
        ),
    ),
)
def test_employee_serializer(position_fixture, test_input, expected_outcome):
    if test_input["name"] != "special_case":
        test_input["position"] = position_fixture.pk
    ser = serializers.EmployeesSerializer(data=test_input)
    assert ser.is_valid() == expected_outcome


@pytest.mark.django_db
@pytest.mark.parametrize(
    "test_input,expected_outcome",
    (
        (
            {"category": "l", "caretaker": None},
            True,
        ),
        ({"category": None, "caretaker": None}, False),
        ({"category": "l", "caretaker": "special"}, True),
    ),
)
def test_cage_serializer(employee_fixture, test_input, expected_outcome):
    if test_input["caretaker"] != "special":
        test_input["caretaker"] = employee_fixture.pk
    else:
        test_input["caretaker"] = None
    ser = serializers.CagesSerializer(data=test_input)
    assert ser.is_valid() == expected_outcome


@pytest.mark.django_db
@pytest.mark.parametrize(
    "test_input,expected_outcome",
    (
        ({"kind": "l", "name": "leon", "cage": None, "AdditionalInfo": None}, True),
        ({"kind": None, "name": "leon", "cage": None, "AdditionalInfo": None}, False),
        ({"kind": "l", "name": None, "cage": None, "AdditionalInfo": None}, False),
        (
            {"kind": "l", "name": "leon", "cage": "special", "AdditionalInfo": None},
            True,
        ),
        (
            {"kind": "a", "name": "leon", "cage": "special", "AdditionalInfo": None},
            False,
        ),
    ),
)
def test_animal_serializer(cage_fixture, test_input, expected_outcome):
    if test_input["cage"] != "special":
        test_input["cage"] = cage_fixture.pk
    else:
        test_input["cage"] = None
    ser = serializers.AnimalsSerializer(data=test_input)
    assert ser.is_valid() == expected_outcome
