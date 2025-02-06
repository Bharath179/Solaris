import logging
import os


class log_maker:
    @staticmethod
    def log_gen():
        log_file = ".\\logs\\solaries.log"
        if os.path.exists(log_file):
            os.remove(log_file)
        logging.basicConfig(filename=log_file,
                            format='%(asctime)s [%(levelname)s] [%(module)s] %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
