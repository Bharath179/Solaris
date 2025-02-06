import time
import pytest
from utilities.read_properties import Read_Config
from page_objects.Login_Page import login_page
from utilities.custom_logger import log_maker
from utilities.screenshot import ScreenshotUtil
from utilities import Xlutility

data_path="test_data/datadriven.xlsx"


class Test_001_login:
    url=Read_Config.get_login_url()
    username=Read_Config.get_username()
    password=Read_Config.get_password()
    logger=log_maker.log_gen()


    @pytest.mark.smoke
    def test_driven_title_verifaction(self,setup):
        self.logger.info(f"Test case to verify the title of the webpage")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.url)
        self.login = login_page(self.driver)
        time.sleep(2)

        rows=Xlutility.get_cell_count(data_path,'Sheet3')
        for row in range(2,rows+1):
            username=Xlutility.read_data(data_path,'Sheet3',row,1)
            password=Xlutility.read_data(data_path,'Sheet3',row,2)
            self.login.set_username(username)
            time.sleep(2)
            self.login.set_password(password)
            time.sleep(2)
            self.login.click_login()
            time.sleep(2)

            if self.driver.title == "Solar Plant Monitoring":
                self.logger.info("The title of the webpage is correct and it is verified")
                assert True
            else:
                ScreenshotUtil.take_screenshot(self.driver, "test_title_verifaction")
                self.logger.info("The title of the webpage is incorrect and it is verified")
                self.driver.quit()
                assert False

            self.login.click_demo_user()
            time.sleep(2)
            self.login.click_logout_btn()
        self.driver.quit()

    @pytest.mark.regression
    def test_click_on_remember_me(self,setup):
        self.logger.info(f"Test case to click on remember me checkbox")
        self.driver=setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.login=login_page(self.driver)
        time.sleep(2)
        remember_me_checkbox = self.login.click_remember_me()

        if remember_me_checkbox is None or not remember_me_checkbox.is_enabled():
            ScreenshotUtil.take_screenshot(self.driver, "test_click_on_remember_me")
            self.logger.info("CheckBox has not been enabled and screenshot is captured...")
            assert True
        else:
            self.logger.info("CheckBox has been enabled...")
            assert False
        time.sleep(2)
        self.driver.quit()

    @pytest.mark.sanity
    def test_forget_link(self, setup):
        self.logger.info(f"Test case to verify the forget link present on login page or not")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.login = login_page(self.driver)
        time.sleep(2)

        page_source = self.driver.page_source

        if "Forgot Password?" in page_source:
            self.logger.info("The 'Forgot Password' link is present in the page source.")
            ScreenshotUtil.take_screenshot(self.driver, "test_forget_link")
        else:
            self.logger.error("The 'Forgot Password' link is NOT present in the page source.")
            raise AssertionError("The 'Forgot Password' link was not found on the page.")

        time.sleep(2)
        self.driver.quit()
