import logging

# logging settings

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app.log'), # Log to a file
        logging.StreamHandler() # Log to console
    ]
    )

logger = logging.getLogger('ArithmeticApp')

def add(x, y):
    logger.debug(f'Adding {x} and {y}')
    return x + y

def subtract(x, y):
    logger.debug(f'Subtracting {y} from {x}')
    return x - y

def multiply(x, y):
    logger.debug(f'Multiplying {x} and {y}')
    return x * y

def divide(x, y):
    try:
        res = x / y
        logger.debug(f'Dividing {x} by {y}')
        return res
    except ZeroDivisionError:
        logger.error('Attempted to divide by zero')
        return None
    
add(10, 5)
subtract(10, 5)
multiply(10, 5)
divide(10, 0)  # This will log an error