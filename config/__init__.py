
import logging
import sys

config = None

def setupConfigAndLogging(environment):
    global config

    try: 
        config = __import__("config." + environment , fromlist=[environment])
    except ImportError:
        sys.exit("Unknown environment. Please create config/" + environment + \
                 ".py") 

    handler = logging.FileHandler(config.log_file)
    handler.setFormatter(logging.Formatter(config.log_format))

    root_logger = logging.getLogger("")
    root_logger.setLevel(logging.getLevelName(config.global_log_level))
    root_logger.addHandler(handler)

    for log_path in config.log_levels:
        logger = logging.getLogger(log_path)
        logger_level = config.log_levels[log_path]
        logger.setLevel(logging.getLevelName(logger_level))
        logger.propagate = 0
        logger.addHandler(handler)