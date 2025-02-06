import logging
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Settings:
    navigation_bar_xpath = "//div[@class='group relative flex flex-col justify-between px-2 pb-4 h-screen']"
    settings_bar_xpath="//p[text()='Settings']"
    user_bar_xpath="//p[text()='User']"
    new_user_xpath="(//button[@type='button'])[3]"
    first_name_xpath="(//input[@type='text'])[1]"
    last_name_xpath="(//input[@type='text'])[2]"
    username_txt_field_xpath="(//input[@type='text'])[3]"
    email_txt_field_xpath="(//input[@type='text'])[4]"
    password_txt_field_xpath="(//input[@type='password'])[1]"
    conform_txt_field_xpath="(//input[@type='password'])[2]"
    select_role_xpath="(//button[@type='button'])[3]"
    slect_option_xpath="//div[text()='Technician']"
    create_new_user_xpath="//button[text()='Create']"

    def __init__(self, driver):
        self.driver = driver

    def get_navigation_bar(self):
        navigation = self.driver.find_element(By.XPATH, self.navigation_bar_xpath)
        action = ActionChains(self.driver)
        time.sleep(2)
        action.move_to_element(navigation).perform()
        return self.driver.find_element(By.XPATH, self.navigation_bar_xpath)

    def click_settings_tab(self):
        self.driver.find_element(By.XPATH,self.settings_bar_xpath).click()

    def click_user_tab(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        user_tab = self.driver.find_element(By.XPATH, self.user_bar_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", user_tab)
        user_tab.click()

    def click_newuser_btn(self):
        self.driver.find_element(By.XPATH, self.new_user_xpath).click()

    def set_first_name(self,firstname):
        self.driver.find_element(By.XPATH,self.first_name_xpath).send_keys(firstname)

    def set_last_name(self,lastname):
        self.driver.find_element(By.XPATH,self.last_name_xpath).send_keys(lastname)

    def set_username(self, username):
        self.driver.find_element(By.XPATH, self.username_txt_field_xpath).send_keys(username)

    def set_email(self, email):
        self.driver.find_element(By.XPATH, self.email_txt_field_xpath).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.password_txt_field_xpath).send_keys(password)

    def set_conform_password(self, conpass):
        self.driver.find_element(By.XPATH, self.conform_txt_field_xpath).send_keys(conpass)

    def click_user_role(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        user_role = self.driver.find_element(By.XPATH, self.select_role_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", user_role)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(user_role))

        # Check if the element is clickable; raise RuntimeError if it's not
        if not user_role.is_enabled() or not user_role.is_displayed():
            raise RuntimeError(f"The user role element at {self.select_role_xpath} is not clickable.")
        else:
            logging.info("The user role element is enabled(clicked)")
        self.driver.execute_script("arguments[0].click();", user_role)

    def select_option_from_user_role(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        user_option = self.driver.find_element(By.XPATH, self.slect_option_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", user_option)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(user_option))

        # Check if the element is clickable; raise RuntimeError if it's not
        if not user_option.is_enabled() or not user_option.is_displayed():
            raise RuntimeError(f"The user option element at {self.slect_option_xpath} is not clickable.")
        else:
            logging.info("The user option selected")
        user_option.click()

    def click_new_user_btn(self):
        self.driver.find_element(By.XPATH, self.create_new_user_xpath).click()
