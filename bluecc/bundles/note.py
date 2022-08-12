import proto_disp_pb2
from extra.common_note_pb2 import NoteDataData

class Note(object):
    def __init__(self, connector, region_id: str):
        self.connector=connector
        self.stub=connector.stub
        self.region_id=region_id

    def create_note(self, note_data: NoteDataData):
        response = self.stub.Dispatch(proto_disp_pb2.DispParams(
            path='Note/createNote',
            region_id=self.region_id,
            param_data=note_data.SerializeToString()
        ))
        return response

    def create_note_with_args(self, **kwargs):
        return self.create_note(NoteDataData(**kwargs))

    def get_note(self, bundle_id: str) -> NoteDataData:
        response = self.stub.Dispatch(proto_disp_pb2.DispParams(
            path='Note/getBundle',
            region_id=self.region_id,
            bundle_id=bundle_id
        ))
        note_msg = NoteDataData()
        response.result_object.Unpack(note_msg)
        return note_msg


def for_notes(region_id: str) -> Note:
    from bluecc.bundles.connector import bundles_connector
    return Note(bundles_connector, region_id)

