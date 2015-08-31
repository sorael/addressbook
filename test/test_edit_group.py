# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group_name(gen):
    if gen.group.count() == 0:
        gen.group.create(Group(name="test"))
    gen.group.edit_first_group(Group(name="New name"))


def test_edit_group_header(gen):
    if gen.group.count() == 0:
        gen.group.create(Group(header="test"))
    gen.group.edit_first_group(Group(header="New header"))


def test_edit_group_footer(gen):
    if gen.group.count() == 0:
        gen.group.create(Group(footer="test"))
    gen.group.edit_first_group(Group(footer="New footer"))
