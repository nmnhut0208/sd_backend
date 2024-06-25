import logging
from datetime import datetime
from logging.handlers import RotatingFileHandler
from pythonjsonlogger import jsonlogger
import config

class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get('timestamp'):
            # this doesn't use record.created, so it is slightly off
            now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            log_record['timestamp'] = now
        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname

class Logger:
    def __init__(self, log_file_path, name: str='serversdk', max_length: int=256):
        self.max_length = max_length
        self.logger = logging.getLogger(name)
        self.logger.setLevel(config.LOG_LEVEL)
        #stream handler
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(CustomJsonFormatter())
        #file handler
        file_handler = RotatingFileHandler(log_file_path,
                                           maxBytes=config.LOG_MAX_SIZE_BYTES,
                                           backupCount=5)
        file_handler.setFormatter(CustomJsonFormatter())
        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)

    def _validate_data(self, data: dict):
        for k, v in data.items():
            if isinstance(v, str) and len(v) > self.max_length:
                data[k] = v[:self.max_length] + '...'
        return data

    def info(self, data: dict):
        self.logger.info(self._validate_data(data))

    def error(self, data: dict):
        self.logger.error(self._validate_data(data))
