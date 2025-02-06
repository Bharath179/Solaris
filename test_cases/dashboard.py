import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.read_properties import Read_Config
from page_objects.Login_Page import login_page
from page_objects.Dashboard import Dashboard
from utilities.custom_logger import log_maker
from utilities.screenshot import ScreenshotUtil


class Test_Dashboard:
    url = Read_Config.get_login_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    logger = log_maker.log_gen()

    def test_visibility_of_navigation_bar(self,setup):
        self.logger.info("Test case to verify the visibility of navigation bar")
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

        self.dashboard = Dashboard(self.driver)
        navigation_bar=self.dashboard.get_navigation_bar()
        if navigation_bar.is_displayed():
            self.logger.info("Navigation bar is visible as expected.")
        else:
            ScreenshotUtil.take_screenshot(self.driver, "test_visibility_of_navigation_bar")
            raise RuntimeError("Navigation bar is not visible. Test failed.")

        self.logger.info("Click on dropdown and select first option")
        self.dashboard.click_on_dropdown()
        time.sleep(2)
        self.dashboard.get_select_first_option()
        time.sleep(2)
        self.dashboard.get_date()
        time.sleep(2)

        """self.logger.info("Selecting the date from the calender")
        date_to_select=self.dashboard.get_paricular_date()
        # WebDriverWait(self.driver, 10).until(EC.staleness_of(date_to_select))
        # date_to_select = self.dashboard.get_paricular_date()
        if date_to_select.is_selected():
            self.logger.info("Date has been selected")
        else:
            ScreenshotUtil.take_screenshot(self.driver, "test_visibility_of_navigation_bar")
            self.logger.info("Date has been not selected")
            #raise RuntimeError("Date has been not selected")"""
        time.sleep(2)

        self.logger.info("Getting the station details")
        station_details = self.dashboard.get_station_details()
        self.logger.info(f"Station details: {station_details}")
        time.sleep(2)
        self.driver.quit()
