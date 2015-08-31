# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(gen):
    if gen.group.count() == 0:
        gen.group.create(Group(name="test"))
    gen.group.delete_first_group()
