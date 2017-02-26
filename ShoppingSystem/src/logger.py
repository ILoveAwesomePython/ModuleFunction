#日志模块记录，账单
import logging
from config import settings

def logger(logger_type):
    logger = logging.getLogger(logger_type)
    logger.setLevel(settings.LOG_LEVEL)

    log_file = "%s/log/%s" % (settings.BASE_DIR, settings.LOG_TYPES[logger_type])
    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOG_LEVEL)
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger



