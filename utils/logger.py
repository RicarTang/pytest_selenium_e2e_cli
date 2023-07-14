from loguru import logger
import config

def log_util():
    """日志管理"""
    logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
    logger.add("file_{time}.log")
    return logger