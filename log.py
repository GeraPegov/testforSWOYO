import logging 

def setup_logger():
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler('app.log')
    file_handler.setFormatter(formatter)


    logging.basicConfig(
        level=logging.INFO,
        handlers=[file_handler]
    )
