# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_delete_some_group(gen):
    if gen.group.count() == 0:
        gen.group.create(Group(name="test"))
    old_groups = gen.group.get_group_list()
    index = randrange(len(old_groups))
    gen.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == gen.group.count()
    new_groups = gen.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups
