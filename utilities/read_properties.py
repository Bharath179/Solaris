import configparser
import os


class Read_Config:
    config = configparser.RawConfigParser()

    @staticmethod
    def load_config():
        file_path = ".\\configurations\\config.ini"
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Configuration file not found at: {file_path}")
        Read_Config.config.read(file_path)

        # Check if 'common data' section exists
        if not Read_Config.config.has_section('common data'):
            raise configparser.NoSectionError('common data')

    @staticmethod
    def get_login_url():
        Read_Config.load_config()
        url = Read_Config.config.get('common data', 'url_of_webpage')
        return url

    @staticmethod
    def get_username():
        Read_Config.load_config()
        email = Read_Config.config.get('common data', 'email')
        return email

    @staticmethod
    def get_password():
        Read_Config.load_config()
        password = Read_Config.config.get('common data', 'password')
        return password
