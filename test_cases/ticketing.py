import logging
import time

from page_objects.Login_Page import login_page
from utilities.custom_logger import log_maker
from utilities.read_properties import Read_Config
from page_objects.Ticketing import Ticketing
from utilities.screenshot import ScreenshotUtil


class Test_Ticketing:
    url = Read_Config.get_login_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    logger = log_maker.log_gen()

    def test_raise_new_ticket_issue(self, setup):
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

        self.ticket = Ticketing(self.driver)
        navigation_bar = self.ticket.get_navigation_bar()
        if navigation_bar.is_displayed():
            self.logger.info("Navigation bar is visible as expected.")
        else:
            ScreenshotUtil.take_screenshot(self.driver, "test_visibility_of_navigation_bar")
            raise RuntimeError("Navigation bar is not visible. Test failed.")

        actions = [
            self.ticket.click_ticketing_bar,
            self.ticket.click_ticket_button,
            self.ticket.click_category_dropdown,
            self.ticket.click_select_category_issue,
            self.ticket.click_priority_dropdown,
            self.ticket.select_option_from_priority_dropdown,
            self.ticket.click_user_dropdown,
            self.ticket.select_option_from_user_dropdown,
            self.ticket.click_on_issue_time,
            self.ticket.select_date_from_calender,
            self.ticket.select_textarea_field
        ]

        # Loop through the actions and execute each one with a short delay
        for action in actions:
            action()
            time.sleep(2)

        time.sleep(5)
        file_upload = self.ticket.click_on_attachment_field()
        if file_upload.is_displayed():
            logging.info("File has been uploaded successfully")
        else:
            ScreenshotUtil.take_screenshot(self.driver, "test_visibility_of_navigation_bar")
            raise RuntimeError("Failed to upload file")
        time.sleep(5)
        self.ticket.click_on_create_button()
        time.sleep(2)
        self.driver.quit()
