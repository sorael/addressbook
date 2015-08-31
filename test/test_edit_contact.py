# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact_firstname(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(firstname="test"))
    gen.contact.edit_first_contact(Contact(firstname="New firstname"))


def test_edit_contact_middlename(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(middlename="test"))
    gen.contact.edit_first_contact(Contact(middlename="New middlename"))


def test_edit_contact_lastname(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(lastname="test"))
    gen.contact.edit_first_contact(Contact(lastname="New lastname"))


def test_edit_contact_nickname(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(nickname="test"))
    gen.contact.edit_first_contact(Contact(nickname="New nickname"))


def test_edit_contact_photo(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(photo=""))
    gen.contact.edit_first_contact(Contact(photo="New photo"))


def test_edit_contact_title(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(title="test"))
    gen.contact.edit_first_contact(Contact(title="New title"))


def test_edit_contact_company(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(company="test"))
    gen.contact.edit_first_contact(Contact(company="New company"))


def test_edit_contact_address(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(address="test"))
    gen.contact.edit_first_contact(Contact(address="New address"))


def test_edit_contact_home(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(home="test"))
    gen.contact.edit_first_contact(Contact(home="New home"))


def test_edit_contact_mobile(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(mobile="test"))
    gen.contact.edit_first_contact(Contact(mobile="New mobile"))


def test_edit_contact_work(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(work="test"))
    gen.contact.edit_first_contact(Contact(work="New work"))


def test_edit_contact_fax(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(fax="test"))
    gen.contact.edit_first_contact(Contact(fax="New fax"))


def test_edit_contact_email2(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(email2="test"))
    gen.contact.edit_first_contact(Contact(email2="New email2"))


def test_edit_contact_email3(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(email3="test"))
    gen.contact.edit_first_contact(Contact(email3="New email3"))


def test_edit_contact_homepage(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(homepage="test"))
    gen.contact.edit_first_contact(Contact(homepage="New homepage"))


def test_edit_contact_bday(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(bday="6"))
    gen.contact.edit_first_contact(Contact(bday="6"))


def test_edit_contact_bmonth(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(bmonth="July"))
    gen.contact.edit_first_contact(Contact(bmonth="July"))


def test_edit_contact_byear(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(byear="1111"))
    gen.contact.edit_first_contact(Contact(byear="1111"))


def test_edit_contact_aday(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(aday="6"))
    gen.contact.edit_first_contact(Contact(aday="6"))


def test_edit_contact_amonth(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(amonth="July"))
    gen.contact.edit_first_contact(Contact(amonth="July"))


def test_edit_contact_ayear(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(ayear="test"))
    gen.contact.edit_first_contact(Contact(ayear="1111"))


def test_edit_contact_address2(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(address2="test"))
    gen.contact.edit_first_contact(Contact(address2="New address2"))


def test_edit_contact_phone2(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(phone2="test"))
    gen.contact.edit_first_contact(Contact(phone2="New phone2"))


def test_edit_contact_notes(gen):
    if gen.contact.count() == 0:
        gen.contact.create(Contact(notes="test"))
    gen.contact.edit_first_contact(Contact(notes="New notes"))
