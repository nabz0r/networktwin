import logging
import logging.config
import os
from datetime import datetime

def setup_logging(log_level=logging.INFO):
    """Configuration centralisée du logging"""
    log_dir = os.path.join(os.getcwd(), 'logs')
    os.makedirs(log_dir, exist_ok=True)

    log_filename = datetime.now().strftime('networktwin_%Y-%m-%d.log')
    log_path = os.path.join(log_dir, log_filename)

    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            },
            'performance': {
                'format': '%(asctime)s - PERFORMANCE - %(message)s'
            }
        },
        'handlers': {
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'standard'
            },
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': log_path,
                'formatter': 'standard'
            },
            'performance': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': os.path.join(log_dir, 'performance.log'),
                'formatter': 'performance'
            }
        },
        'loggers': {
            '': {  # Root logger
                'handlers': ['console', 'file'],
                'level': log_level,
                'propagate': True
            },
            'performance': {
                'handlers': ['performance'],
                'level': 'INFO',
                'propagate': False
            }
        }
    }

    logging.config.dictConfig(logging_config)
    return logging.getLogger(__name__)

# Décorateur pour mesurer les performances
def log_performance(func):
    import time
    import functools
    import logging

    performance_logger = logging.getLogger('performance')

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        performance_logger.info(f"{func.__name__} executed in {(end_time - start_time)*1000:.2f} ms")
        return result
    
    return wrapper