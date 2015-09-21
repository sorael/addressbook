# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from data.groups import test_data


def test_add_group(gen, db, json_groups):
    group = json_groups
    old_groups = db.get_group_list()
    gen.group.create(group)
    # assert len(old_groups) + 1 == gen.group.count()
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# @pytest.mark.parametrize("group", test_data, ids=[str(x) for x in test_data])
# def test_add_group(gen, group):
#     old_groups = gen.group.get_group_list()
#     gen.group.create(group)
#     assert len(old_groups) + 1 == gen.group.count()
#     new_groups = gen.group.get_group_list()
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)