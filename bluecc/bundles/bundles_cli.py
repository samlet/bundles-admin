import grpc
import slugid
import proto_disp_pb2
import proto_disp_pb2_grpc
from extra.common_note_pb2 import NoteDataData
from routines_pb2 import FixedPoint


class BundlesCli(object):
    def __int__(self):
        # self.bridge=BundlesBridgeConnector()
        pass

    def version(self):
        """
        $ python -m bluecc.bundles.bundles_cli version
        :return:
        """
        from bluecc.bundles.bundles_bridge import bridge
        # bridge = BundlesBridgeConnector()
        print(bridge.version)
        # print('1.0')

    def some_test(self):
        """
        $ . env.sh
        $ python -m bluecc.bundles.bundles_cli some_test
        :return:
        """
        print("fixed-point", FixedPoint(value=5))

        # https://developers.google.com/protocol-buffers/docs/pythontutorial#parsing-and-serialization
        # SerializeToString(): serializes the message and returns it as a string.
        # Note that the bytes are binary, not text; we only use the str type
        # as a convenient container.
        # ParseFromString(data): parses a message from the given string.
        print(FixedPoint(value=5).SerializeToString())
        # output: b'\x08\x05'

    def grpc_test(self):
        """
        $ python -m bluecc.bundles.bundles_cli grpc_test
        :return:
        """
        # https://grpc.io/docs/languages/python/quickstart/
        with grpc.insecure_channel('localhost:9667') as channel:
            stub = proto_disp_pb2_grpc.ProtoDispServiceStub(channel)
            note_id=slugid.nice()
            response = stub.Dispatch(proto_disp_pb2.DispParams(
                path='Note/createNote',
                region_id='default',
                param_data=NoteDataData(
                    note_id=note_id,
                    note_name='test-note',
                    note_info='just a note')
                .SerializeToString()
            ))
            print("create note: ",
                  note_id,
                  response.result,
                  response.message)

            response = stub.Dispatch(proto_disp_pb2.DispParams(
                path='Note/getBundle',
                region_id='default',
                bundle_id=note_id
            ))
            note_msg=NoteDataData()
            response.result_object.Unpack(note_msg)
            print("get note: ",
                  response.result,
                  response.result_object.type_url,
                  note_msg)


if __name__ == '__main__':
    import fire

    fire.Fire(BundlesCli)
