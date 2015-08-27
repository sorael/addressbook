
class SessionHelper:
    def __init__(self, gen):
        self.gen = gen

    def logout(self):
        driver = self.gen.driver
        driver.find_element_by_link_text("Logout").click()

    def login(self, username, password):
        driver = self.gen.driver
        self.gen.open_home_page()
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_id("LoginForm").click()
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
