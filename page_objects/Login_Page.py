from selenium.webdriver.common.by import By


class login_page:
    username_txt_field_id = "name"
    password_txt_field_xpath = "//input[@type='password']"
    login_btn_xpath = "//button[text()='Sign In']"
    click_on_demo_user_xpath = "//button[@type='button']//span[text()='Demo User | Admin']"
    click_on_logout_btn_xpath = "//div[text()='Logout']"
    click_on_remember_me_xpath = "//input[@type='checkbox']"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.ID, self.username_txt_field_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.password_txt_field_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()

    def click_demo_user(self):
        self.driver.find_element(By.XPATH, self.click_on_demo_user_xpath).click()

    def click_logout_btn(self):
        self.driver.find_element(By.XPATH, self.click_on_logout_btn_xpath).click()

    def click_remember_me(self):
        checkbox_element = self.driver.find_element(By.XPATH, self.click_on_remember_me_xpath)
        checkbox_element.click()
        return checkbox_element
