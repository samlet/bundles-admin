import grpc

import proto_disp_pb2_grpc


class BundlesConnector(object):
    def __init__(self):
        self.channel=grpc.insecure_channel('localhost:9667')
        self.stub = proto_disp_pb2_grpc.ProtoDispServiceStub(self.channel)

bundles_connector=BundlesConnector()
