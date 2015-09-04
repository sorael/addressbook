# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group_name(gen):
    if gen.group.count() == 0:
        gen.group.create(Group(name="test"))
    old_groups = gen.group.get_group_list()
    group = Group(name="New name")
    group.id = old_groups[0].id
    gen.group.edit_first_group(group)
    assert len(old_groups) == gen.group.count()
    new_groups = gen.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_edit_group_header(gen):
#     if gen.group.count() == 0:
#         gen.group.create(Group(header="test"))
#     old_groups = gen.group.get_group_list()
#     group = Group(header="New header")
#     gen.group.edit_first_group(group)
#     new_groups = gen.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_edit_group_footer(gen):
#     if gen.group.count() == 0:
#         gen.group.create(Group(footer="test"))
#     old_groups = gen.group.get_group_list()
#     group = Group(footer="New footer")
#     gen.group.edit_first_group(group)
#     new_groups = gen.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
