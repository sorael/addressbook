# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(gen):
    if gen.group.count() == 0:
        gen.group.create(Group(name="test"))
    old_groups = gen.group.get_group_list()
    gen.group.delete_first_group()
    assert len(old_groups) - 1 == gen.group.count()
    new_groups = gen.group.get_group_list()
    old_groups[0:1] = []
    assert old_groups == new_groups
