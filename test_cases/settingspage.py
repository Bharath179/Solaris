import time

from page_objects.Login_Page import login_page
from utilities.custom_logger import log_maker
from utilities.read_properties import Read_Config
from page_objects.Settings import Settings
from utilities.screenshot import ScreenshotUtil


class TestSettings:
    url = Read_Config.get_login_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    logger = log_maker.log_gen()

    def test_to_create_new_user(self, setup):
        self.logger.info("Test case to raise new ticket")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.url)
        self.login = login_page(self.driver)
        time.sleep(2)
        self.login.set_username(self.username)
        time.sleep(2)
        self.login.set_password(self.password)
        time.sleep(2)
        self.login.click_login()
        time.sleep(2)

        self.setting=Settings(self.driver)
        navigation_bar = self.setting.get_navigation_bar()
        if navigation_bar.is_displayed():
            self.logger.info("Navigation bar is visible as expected.")
        else:
            ScreenshotUtil.take_screenshot(self.driver, "test_visibility_of_navigation_bar")
            raise RuntimeError("Navigation bar is not visible. Test failed.")

        time.sleep(2)
        self.setting.click_settings_tab()
        time.sleep(2)
        self.setting.click_user_tab()
        time.sleep(2)
        self.setting.click_newuser_btn()
        time.sleep(2)
        self.setting.set_first_name("Bharath")
        time.sleep(2)
        self.setting.set_last_name("Kumar")
        time.sleep(2)
        self.setting.set_username("Bharath Kumar")
        time.sleep(2)
        self.setting.set_email("bharath@gmail.com")
        time.sleep(2)
        self.setting.set_password("bharath@123")
        time.sleep(2)
        self.setting.set_conform_password("bharath@123")
        time.sleep(2)
        self.setting.click_user_role()
        time.sleep(2)
        self.setting.select_option_from_user_role()
        time.sleep(2)
        self.setting.click_new_user_btn()
        time.sleep(2)
        self.driver.quit()