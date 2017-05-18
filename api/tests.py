import pytest
from api.app import get_race
from falcon import errors

def test_race_bad():
    with pytest.raises(errors.HTTPBadRequest):
        get_race('race that doesnt exist')

def test_race_case():
    assert get_race('Human') == get_race('human')
