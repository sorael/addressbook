# -*- coding: utf-8 -*-
from fixture.general import General
import pytest


fixture = None


@pytest.fixture
def gen(request):
    global fixture
    if fixture is None:
        fixture = General()
    else:
        if not fixture.is_valid():
            fixture = General()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy_fixture()
    request.addfinalizer(fin)
    return fixture
