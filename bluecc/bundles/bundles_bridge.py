import logging

from py4j.java_gateway import JavaGateway, JavaObject, GatewayParameters
from py4j.java_gateway import java_import, get_field

logger = logging.getLogger(__name__)

class BundlesBridgeConnector(object):
    def __init__(self, host="localhost", port=25333, callback_port=25334):
        logger.info("connect to py4j-gateway %s %d"%(host, port))

        # self.gateway = JavaGateway()  # connect to the JVM
        self.gateway = JavaGateway(python_proxy_port=callback_port,
                                   gateway_parameters=GatewayParameters(address=host, port=port))
        self.regions = self.gateway.entry_point.getRegions()
        self.standalone=self.gateway.entry_point.getStandalone()
        self.acctg= self.standalone.getAcctgSession()
        self.version=self.gateway.version()

        self.j = self.gateway.new_jvm_view()
        self.srv_rpc=None
        java_import(self.j, 'java.util.*')

        logger.info(f"connector version {self.version}")

