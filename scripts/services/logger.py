import logging
import time

if __name__ == "__main__":

    print(f"Start")
    time.sleep(1)

    logging_in_file = False  # True - file, False - console
    log_file_name = 'log.txt'
    logging_level = logging.INFO
    logging_format = '%(asctime)s - %(levelname)s - %(message)s'
    format_datetime = '%Y-%m-%d %H:%M:%S'

    if logging_in_file:  # Logging format
        logging.basicConfig(  # File
            filename=log_file_name,
            filemode='a',
            format=logging_format,
            datefmt=format_datetime,
            level=logging_level
        )
        logging.info("Log started")
    else:  # Console
        logging.basicConfig(
            format=logging_format,
            datefmt=format_datetime,
            level=logging_level
        )

    logging.info("Info")
    logging.error("Error")
    logging.warning("Warning")
