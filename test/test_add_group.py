# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(gen):
    gen.group.create(Group(name="qwqw22qw", header="qwqwqw", footer="qweweqewewe"))


def test_add_empty_group(gen):
    gen.group.create(Group(name="", header="", footer=""))
