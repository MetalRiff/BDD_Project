from selenium.webdriver.common.by import By
from base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    BUTTON = (By.ID, 'login-button')
    ERROR = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')

    def navigate_to_login_page(self):
        self.chrome.get("https://www.saucedemo.com")

    def insert_correct_username(self):
        self.chrome.find_element(*self.USERNAME).send_keys("standard_user")

    def insert_incorrect_username(self):
        self.chrome.find_element(*self.USERNAME).send_keys("incorrect_user")

    def insert_correct_password(self):
        self.chrome.find_element(*self.PASSWORD).send_keys("secret_sauce")

    def insert_incorrect_password(self):
        self.chrome.find_element(*self.PASSWORD).send_keys("invalid_password")

    def click_login_button(self):
        self.chrome.find_element(*self.BUTTON).click()

    def check_error_message(self):
        expected_error_message = 'Epic sadface: Username and password do not match any user in this service'
        actual_error_message = self.chrome.find_element(*self.ERROR).text
        assert expected_error_message == actual_error_message, "Error: Incorrect error message"
