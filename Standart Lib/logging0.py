#!/usr/bin/env python3
import logging
file = 'logi.log'
logging.basicConfig(level=logging.INFO, filename=file, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('это дебаг')
logging.info('это инфа')
logging.warning("Это предупреждение")
logging.error("Это сообщение об ошибке")
logging.critical("Это критическая ошибка")