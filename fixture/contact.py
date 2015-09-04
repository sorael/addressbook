# -*- coding: utf-8 -*-
from model.contact import Contact
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert


class ContactHelper:
    def __init__(self, gen):
        self.gen = gen

    def create(self, contact):
        self.click_add_new_button()
        self.fill_contact_form(contact)
        self.click_submit_button()
        self.return_to_home_page()
        self.contact_cache = None

    def click_add_new_button(self):
        driver = self.gen.driver
        driver.find_element_by_link_text("add new").click()

    def click_submit_button(self):
        driver = self.gen.driver
        driver.find_element_by_name("submit").click()

    def fill_contact_form(self, contact):
        driver = self.gen.driver
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        # self.change_field_value("photo", contact.photo)
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

    def delete_contact_from_contacts_page(self, index):
        driver = self.gen.driver
        self.open_home_page()
        self.select_contact_by_index(index)
        self.delete_button_click()
        driver.switch_to_alert()
        Alert(driver).accept()
        self.return_to_home_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        driver = self.gen.driver
        driver.find_elements_by_name("selected[]")[index].click()

    def open_home_page(self):
        driver = self.gen.driver
        if not (len(driver.find_elements_by_xpath("//input[@value='Send e-Mail']")) == 1):
            driver.find_element_by_link_text("home").click()

    def delete_contact_from_edit_page(self, index):
        self.open_home_page()
        self.edit_button_click(index)
        self.delete_button_click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_button_click(self):
        driver = self.gen.driver
        driver.find_element_by_xpath("//input[@value='Delete']").click()

    def return_to_home_page(self):
        driver = self.gen.driver
        driver.find_element_by_link_text("home").click()

    def add_next(self):
        driver = self.gen.driver
        driver.find_element_by_link_text("add next").click()

    def edit_contact_from_home_page(self, index, new_contact_data):
        driver = self.gen.driver
        self.open_home_page()
        self.edit_button_click(index)
        self.fill_contact_form(new_contact_data)
        driver.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_contact_from_contact_page(self, index, new_contact_data):
        driver = self.gen.driver
        self.open_home_page()
        self.detail_button_click(index)
        driver.find_element_by_name("modifiy").click()
        self.fill_contact_form(new_contact_data)
        driver.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_button_click(self, index):
        driver = self.gen.driver
        driver.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def detail_button_click(self, index):
        driver = self.gen.driver
        driver.find_elements_by_xpath("//img[@title='Details']")[index].click()

    def count(self):
        driver = self.gen.driver
        return len(driver.find_elements_by_name("selected[]"))

    def create_after_added_contact(self, contact):
        self.click_add_new_button()
        self.fill_contact_form(contact)
        self.click_submit_button()
        self.add_next()
        self.create(contact)
        self.contact_cache = None

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            driver = self.gen.driver
            self.contact_cache = []
            for i in driver.find_elements_by_xpath("//tr[@name='entry']"):
                firstname = i.find_element_by_xpath("td[3]").text
                contact_id = i.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=firstname, id=contact_id))
        return list(self.contact_cache)
