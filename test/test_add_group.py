# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(gen):
    old_groups = gen.group.get_group_list()
    group = Group(name="qwqw22qw", header="qwqwqw", footer="qweweqewewe")
    gen.group.create(group)
    assert len(old_groups) + 1 == gen.group.count()
    new_groups = gen.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_add_empty_group(gen):
#     old_groups = gen.group.get_group_list()
#     group = Group(name="", header="", footer="")
#     gen.group.create( group)
#     new_groups = gen.group.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
