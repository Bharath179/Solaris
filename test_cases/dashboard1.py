import time

from utilities.custom_logger import log_maker
from utilities.read_properties import Read_Config
from page_objects.Dash_board import Dash_board
from utilities.screenshot import ScreenshotUtil


class Test_Dashboard:
    url = Read_Config.get_login_url()
    logger = log_maker.log_gen()

    def test_dashboard_visible_after_navigating_to_solaris_url(self, setup):
        self.logger.info("Test case for verifying dashboard is visible "
                         "after entering solaris url")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.dashboard = Dash_board(self.driver)
        self.dashboard.get_dash_board_txt()
        page_source = self.driver.page_source

        if "Dashboard" in page_source:
            self.logger.info("The 'dashboard' link is present in the page source.")
            #ScreenshotUtil.take_screenshot(self.driver, "test_dashboard_visible_after_navigating_to_solaris_url")
        else:
            raise AssertionError("The 'dashboard' link was not found on the page.")

        actual_title = self.driver.title
        expected_tile = "Solaris"
        if actual_title == expected_tile:
            self.logger.info("The dashboard title is found correct and it is verified")
            #ScreenshotUtil.take_screenshot(self.driver, "test_dashboard_visible_after_navigating_to_solaris_url")
        else:
            raise AssertionError("The dashboard title is found incorrect and it is verified")

        time.sleep(2)
        self.driver.quit()

    def test_to_verify_side_bar_visible_on_dashboard(self, setup):
        self.logger.info("Test for to check navigation bar is present on dashboard")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.dashboard = Dash_board(self.driver)
        side_bar_element = self.dashboard.get_side_bar()
        ScreenshotUtil.take_element_screenshot(side_bar_element, 'test_to_verify_side_bar_visible_on_dashboard')
        self.logger.info("Test completed: Sidebar is visible and screenshot taken.")
        self.driver.quit()

    def test_dashboard_components_visible(self, setup):
        self.logger.info("Test case to verify components present on "
                         "dashboard after displaying dashboard")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.dashboard = Dash_board(self.driver)
        components = self.dashboard.get_components()
        for index, component in enumerate(components, start=1):
            self.logger.info(f"Component {index}: {component.text}")
        time.sleep(5)
        self.driver.quit()

    def test_station_text_present_on_dashboard(self, setup):
        self.logger.info("Test case to verify the station text present on dashboard or not")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.dashboard = Dash_board(self.driver)

        station_text = self.dashboard.get_station_txt()
        self.logger.info("Station text is: %s", station_text)

        # check for station link present on dashboard or not
        page_source = self.driver.page_source
        if "Station" in page_source:
            self.logger.info("The station text present on dashboard")
        else:
            raise RuntimeError("The station text is not visible on dashboard")
        time.sleep(2)
        self.driver.quit()

    def test_horizontal_alignment(self, setup):
        self.logger.info("Test case to verify horizontal alignment")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.dashboard = Dash_board(self.driver)

        # Get Y positions
        y1 = self.dashboard.station_card().location['y']
        y2 = self.dashboard.generation_card().location['y']
        y3 = self.dashboard.weather_card().location['y']

        tolerance = 5
        aligned = abs(y1 - y2) <= tolerance and abs(y2 - y3) <= tolerance

        if not aligned:
            #ScreenshotUtil.take_screenshot(self.driver, 'test_horizontal_alignment')
            raise RuntimeError(
                f"Horizontal alignment failed:\n"
                f"Station Y: {y1}, Generation Y: {y2}, Weather Y: {y3}\n"
                f"Tolerance: {tolerance}px"
            )

        time.sleep(2)
        self.driver.quit()

    def test_hierarchy_of_stations(self, setup):
        self.logger.info("Test to verify hierarchy of stations")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.dashboard = Dash_board(self.driver)
        station_elements = self.dashboard.get_station_zones()
        for station in station_elements:
            self.logger.info("Station text's is: %s", station.text)

        time.sleep(2)
        self.driver.quit()

    def test_particular_region_station(self, setup):
        self.logger.info("Test case for to test particular region")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.dashboard = Dash_board(self.driver)
        self.dashboard.get_station_zones()
        time.sleep(5)
        self.dashboard.get_zone_details("East", ["Assam", "Manipur"])
        self.dashboard.get_zone_details("North", ["Bihar", "Rajasthan"])
        self.dashboard.get_zone_details("South", ["Karnataka", "Andhra Pradesh"])
        self.dashboard.get_zone_details("West", ["Gujarat", "Maharashtra"])
        time.sleep(2)
        self.driver.quit()

    def test_validate_table(self, setup):
        self.logger.info("Test case to validate table and check inverter status")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.dashboard = Dash_board(self.driver)
        active, inactive = self.dashboard.get_table_values()

        # Optional assertions or checks
        assert active or inactive, "No inverters found in the table!"
        time.sleep(2)
        self.driver.quit()

