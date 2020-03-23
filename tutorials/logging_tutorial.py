import logging

# logging.warning('Watch Out!')
# logging.info('I told you so.')

logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
