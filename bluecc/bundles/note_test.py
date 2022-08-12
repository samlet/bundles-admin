from slugid import slugid

from bluecc.bundles.note import for_notes
from extra.common_note_pb2 import NoteDataData


def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


def test_create_and_get_note():
    notes = for_notes('default')
    note_id = slugid.nice()
    response = notes.create_note(NoteDataData(
        note_id=note_id,
        note_name='test-note',
        note_info='just a note'))
    print("create note: ",
          note_id,
          response.result,
          response.message)
    assert response.result == 0

    note = notes.get_note(note_id)
    print("get note ->", note)
