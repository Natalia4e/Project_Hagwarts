import logging
import datetime

logging.basicConfig(level=logging.INFO, filename="py_log.log")


def lod_action(mm):
    now = datetime.datetime.now()
    logging.info(f"{now} {mm}")

def log_warn(mm):
    now = datetime.datetime.now()
    logging.warning(f"{now} {mm}")