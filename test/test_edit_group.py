# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group_name(gen):
    gen.group.edit_first_group(Group(name="New name"))


def test_edit_group_header(gen):
    gen.group.edit_first_group(Group(header="New header"))


def test_edit_group_footer(gen):
    gen.group.edit_first_group(Group(footer="New footer"))
