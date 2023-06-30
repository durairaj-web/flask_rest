import logging
import os

from datetime import date
from pathlib import Path
from config.dynaconf import settings

service_directory = Path(__file__).parent
ROOT_DIR = service_directory.parent
LOG_DIR = 'logs'

today = date.today()
tdate = today.strftime("%Y-%m-%d")
FORMATTER = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

info_loggers = {}
debug_loggers = {}
error_loggers = {}
warning_loggers = {}


def info_log(name):
    global info_loggers
    if info_loggers.get(name):
        return info_loggers.get(name)
    else:
        info_logging = logging.getLogger("info")
        info_logging.setLevel(logging.INFO)
        if settings['RUNNING_ENV'] == "local":
            if not os.path.exists(os.path.join(ROOT_DIR, LOG_DIR)):
                os.makedirs(os.path.join(ROOT_DIR, LOG_DIR))
            info_file_handler = logging.FileHandler(os.path.join(ROOT_DIR,  LOG_DIR, 'info-' + tdate + '.log'))
        else:
            info_file_handler = logging.StreamHandler()
        info_file_handler.setFormatter(FORMATTER)
        info_logging.addHandler(info_file_handler)
        info_loggers[name] = info_logging
        return info_logging


def debug_log(dname):
    global debug_loggers
    if debug_loggers.get(dname):
        return debug_loggers.get(dname)
    debug_logging = logging.getLogger("debug")
    debug_logging.setLevel(logging.DEBUG)
    if settings['RUNNING_ENV'] == "local":
        if not os.path.exists(os.path.join(ROOT_DIR, LOG_DIR)):
            os.makedirs(os.path.join(ROOT_DIR, LOG_DIR))
        debug_file_handler = logging.FileHandler(os.path.join(ROOT_DIR, LOG_DIR, 'debug-' + tdate + '.log'))
    else:
        debug_file_handler = logging.StreamHandler()
    debug_file_handler.setFormatter(FORMATTER)
    debug_logging.addHandler(debug_file_handler)
    debug_loggers[dname] = debug_logging
    return debug_logging


def error_log(ename):
    global error_loggers
    if error_loggers.get(ename):
        return error_loggers.get(ename)
    error_logging = logging.getLogger('error')
    error_logging.setLevel(logging.ERROR)
    if settings['RUNNING_ENV'] == "local":
        if not os.path.exists(os.path.join(ROOT_DIR, LOG_DIR)):
            os.makedirs(os.path.join(ROOT_DIR, LOG_DIR))
        error_file_handler = logging.FileHandler(os.path.join(ROOT_DIR, LOG_DIR, 'error-' + tdate + '.log'))
    else:
        error_file_handler = logging.StreamHandler()
    error_file_handler.setFormatter(FORMATTER)
    error_logging.addHandler(error_file_handler)
    error_loggers[ename] = error_logging
    return error_logging


def warning_log(wname):
    global warning_loggers
    if warning_loggers.get(wname):
        return warning_loggers.get(wname)
    warning_logging = logging.getLogger('warning')
    warning_logging.setLevel(logging.WARNING)
    if settings['RUNNING_ENV'] == "local":
        if not os.path.exists(os.path.join(ROOT_DIR, LOG_DIR)):
            os.makedirs(os.path.join(ROOT_DIR, LOG_DIR))
        warning_file_handler = logging.FileHandler(os.path.join(ROOT_DIR, LOG_DIR, 'Warning-' + tdate + '.log'))
    else:
        warning_file_handler = logging.StreamHandler()
    warning_file_handler.setFormatter(FORMATTER)
    warning_logging.addHandler(warning_file_handler)
    warning_loggers[wname] = warning_logging
    return warning_logging


def logger_info(message):
    info_log("Info").info(message)


def logger_error(message):
    error_log("Error").error(message)


def logger_warn(message):
    warning_log("Warn").warning(message)


def logger_debug(message):
    debug_log("Debug").debug(message)
