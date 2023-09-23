import sys
import os
import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler

class AppInsights(object):

    def __init__(self, dsn, **kwargs):
        logger = logging.getLogger(__name__)
        logger.addHandler(AzureLogHandler(connection_string=f'InstrumentationKey={os.environ.get("APPINSIGHTS_INSTRUMENTATIONKEY")}'))

    def report(self):
        pass