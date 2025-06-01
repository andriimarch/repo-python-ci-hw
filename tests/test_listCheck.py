from pytest_steps import test_steps

from methods.list_methods import*

def test_getTeamIdWithValidtoken():
    result = getTeamIdValidToken()
    assert result is not None

def test_getTeamIdWithInvalidtoken():
    result = getTeamIdInValidToken()
    assert result.status_code != 200

def test_createSpace():
    result = createSpace()
    assert result.status_code == 200

def test_getSpace():
    result = getSpace()
    print(result['spaces'][0]['name'])
    assert result['spaces'][0]['name'] is not None

def test_updateSpace():
    result = updateSpace()
    assert result.status_code == 200

def test_removeSpace():
    result = removeSpace()
    assert result.status_code == 200