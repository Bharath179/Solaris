import logging
import os
import time


class ScreenshotUtil:
    @staticmethod
    def take_screenshot(driver, test_name):
        screenshot_folder = ".\\screenshots"

        if not os.path.exists(screenshot_folder):
            os.makedirs(screenshot_folder)
            logging.info("Screenshots directory has been created at: %s", screenshot_folder)
        else:
            logging.info("Screenshots directory already exists at: %s", screenshot_folder)

        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_path = os.path.join(screenshot_folder, "%s_%s.png" % (test_name, timestamp))
        driver.save_screenshot(screenshot_path)
        logging.info("Screenshot saved at %s", screenshot_path)

    @staticmethod
    def take_element_screenshot(element, test_name):

        screenshot_folder = ".\\screenshots"

        if not os.path.exists(screenshot_folder):
            os.makedirs(screenshot_folder)
            logging.info("Screenshots directory has been created at: %s", screenshot_folder)
        else:
            logging.info("Screenshots directory already exists at: %s", screenshot_folder)

        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_path = os.path.join(screenshot_folder, f"{test_name}_element_{timestamp}.png")
        element.screenshot(screenshot_path)
        logging.info("Element screenshot saved at %s", screenshot_path)