import pytest

from validation.script import validation

@pytest.fixture
def test_data_one():
    dictionary = {
        'name': 'Ritik',
        'age': 11,
        'is_disabled': True,
    }

    validation_rule = {
        'name': {'max_length': 15, 'min_length':5},
        'age': {'min_value': 10, 'max_value':21},
        'is_disabled': {'bool': True}
    }

    expected_result = True

    return (dictionary, validation_rule, expected_result)

@pytest.mark.parametrize('data, rule, expected_result',[
    [
        {
            'name': 'Ritik',
            'age': 11,
            'is_disabled': True,
        },
        {
            'name': {'max_length': 15, 'min_length':5},
            'age': {'min_value': 10, 'max_value':21},
            'is_disabled': {'bool': True}
        },
        True
    ],
    [
        {
            'tutorial': 'validation test in python for newbies',
            'time_min': 15,
            'python': False,
        },
        {
            'tutorial': {'max_length': 50, 'min_length':20},
            'time_min': {'min_value': 10, 'max_value':25},
            'python': {'bool': True}
        },
        False
    ]
])


def test_validation(data, rule, expected_result):
    result = validation(data, rule)

    assert result == expected_result

