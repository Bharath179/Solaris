import time
from selenium import webdriver
from utilities.read_properties import Read_Config
from page_objects.Login_Page import login_page
from utilities.custom_logger import log_maker
from utilities.screenshot import ScreenshotUtil


class Test_001_login:
    url=Read_Config.get_login_url()
    username=Read_Config.get_username()
    password=Read_Config.get_password()
    logger=log_maker.log_gen()

    def test_title_verifaction(self):
        self.logger.info("Test case to verify the title of the webpage")
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.url)

        self.login=login_page(self.driver)

        time.sleep(2)
        self.login.set_username(self.username)
        time.sleep(2)
        self.login.set_password(self.password)
        time.sleep(2)
        self.login.click_login()
        time.sleep(2)
        if self.driver.title=="Solar Plant Monitoring":
            self.logger.info("The title of the webpage is correct and it is verified")
            assert True
        else:
            ScreenshotUtil.take_screenshot(self.driver, "test_title_verifaction")
            self.logger.info("The title of the webpage is incorrect and it is verified")
            self.driver.quit()
            assert False
