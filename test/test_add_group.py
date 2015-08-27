# -*- coding: utf-8 -*-
from model.group import Group
from fixture.general import General
import pytest


@pytest.fixture
def gen(request):
    fixture = General()
    request.addfinalizer(fixture.destroy_fixture)
    return fixture


def test_add_group(gen):
    gen.session.login(username="admin", password="secret")
    gen.group.create(Group(name="qwqw22qw", header="qwqwqw", footer="qweweqewewe"))
    gen.session.logout()


def test_add_empty_group(gen):
    gen.session.login(username="admin", password="secret")
    gen.group.create(Group(name="", header="", footer=""))
    gen.session.logout()
