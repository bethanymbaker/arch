import logging
from datetime import datetime

# logging.warning('Watch Out!')
# logging.info('I told you so.')


logging.basicConfig(filename='example.log', level=logging.DEBUG)

logging.info(f"beginning query at {(st := datetime.now())}")
logging.info(f"time to run query = {(datetime.now() - st).total_seconds():3f}")

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')