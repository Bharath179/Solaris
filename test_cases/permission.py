import time

from page_objects.Login_Page import login_page
from utilities.custom_logger import log_maker
from utilities.read_properties import Read_Config
from page_objects.Permission import Permission_page
from utilities.screenshot import ScreenshotUtil


class TestPermission:
    url = Read_Config.get_login_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    logger = log_maker.log_gen()

    def test_to_create_permission_to_user(self, setup):
        self.logger.info("Test case to create permission for user")
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

        self.permission = Permission_page(self.driver)
        navigation_bar = self.permission.get_navigation_bar()
        if navigation_bar.is_displayed():
            self.logger.info("Navigation bar is visible as expected.")
        else:
            ScreenshotUtil.take_screenshot(self.driver, "test_visibility_of_navigation_bar")
            raise RuntimeError("Navigation bar is not visible. Test failed.")

        # Assuming permission is an object with the required methods
        actions = [
            self.permission.click_settings_tab,
            self.permission.click_on_permission_tab,
            self.permission.click_on_permission_newBtn,
        ]

        # Loop through the actions and execute each one
        for action in actions:
            action()
            time.sleep(2)

        self.permission.enter_permission_name("Bharath")
        self.permission.select_checkboxes()
        self.permission.scroll_to_reports()
        self.permission.click_on_createBtn()
        self.permission.check_user_created_or_not()
        self.driver.quit()
