import logging
import os


def logger_config(module) -> logging.Logger:
    """
    usage:
        logger = logger_config(__name__)
        logger.info("__name__")
    """
    formatter = logging.Formatter(
        "===%(asctime)s - %(name)s - %(levelname)s - %(message)s==="
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(module)
    logger.setLevel(os.getenv("LOG_LEVEL", "DEBUG"))
    logger.addHandler(handler)

    return logger
