# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class General:

    def __init__(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def destroy_fixture(self):
        self.driver.quit()
