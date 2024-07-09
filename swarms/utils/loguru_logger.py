from loguru import logger

logger.add(
    "logs/swarms.log",
    level="INFO",
    colorize=True,
    format="<green>{time}</green> <level>{message}</level>",
    backtrace=True,
    diagnose=True,
)


def loguru_logger(file_path: str = "logs/swarms.log"):
    return logger.add(
        file_path,
        level="INFO",
        colorize=True,
        format="<green>{time}</green> <level>{message}</level>",
        backtrace=True,
        diagnose=True,
    )
