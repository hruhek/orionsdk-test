import logging
import os

from dotenv import load_dotenv
from orionsdk import SwisClient
import requests

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


def do_query(query_str):
    load_dotenv()

    # Disable Orion SSL warnings
    requests.packages.urllib3.disable_warnings()

    # Connect to Orion server
    logging.debug('No SwisClient')
    orion_server = os.getenv('ORION_SERVER')
    username = os.getenv('ORION_USER')
    password = os.getenv('ORION_PASSWORD')
    swis = SwisClient(orion_server, username, password)
    logging.debug('SwisClient created')

    # Get a current list of polling engines
    logging.debug('before query')
    queryEngines = swis.query(query_str)
    logging.debug('after query')

    # Assign the list of dictionaries with polling engine information to a variable
    result = queryEngines["results"]
    return result


if __name__ == '__main__':
    logging.info('start')
    result = do_query("SELECT ServerName FROM Orion.Engines")
    logging.info('do_query result: %s' % result)
    logging.info('end')
