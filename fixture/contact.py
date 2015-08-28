# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert


class ContactHelper:
    def __init__(self, gen):
        self.gen = gen

    def create(self, contact):
        driver = self.gen.driver
        driver.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        driver.find_element_by_name("submit").click()
        self.return_to_home_page()

    def fill_contact_form(self, contact):
        driver = self.gen.driver
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("photo", contact.photo)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        if contact.bday is not None:
            Select(driver.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        if contact.bmonth is not None:
            Select(driver.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        self.change_field_value("byear", contact.byear)
        if contact.aday is not None:
            Select(driver.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        if contact.amonth is not None:
            Select(driver.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        driver = self.gen.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        driver = self.gen.driver
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_xpath("//input[@value='Delete']").click()
        driver.switch_to_alert()
        Alert(driver).accept()
        self.return_to_home_page()

    def return_to_home_page(self):
        driver = self.gen.driver
        driver.find_element_by_link_text("home").click()

    def modify_first_contact(self):
        pass
