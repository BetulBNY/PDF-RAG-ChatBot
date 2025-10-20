import logging

def setup_logger(name="ragbot"):
    # Logger oluştur
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # DEBUG, INFO, WARNING, ERROR, CRITICAL

    # Konsola yazdırmak için handler ekle
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Format ayarla
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(console_handler)
    
    return logger


logger = setup_logger()