# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_delete_some_group(gen, db, check_ui):
    if len(db.get_group_list()) == 0:
        gen.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    gen.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == gen.group.count()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(gen.group.get_group_list(), key=Group.id_or_max)
