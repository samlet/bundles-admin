import streamlit as st
from google.protobuf import json_format
from slugid import slugid

from bluecc.bundles.note import for_notes
# from extra.common_note_pb2 import NoteDataData

# def note_panel():
st.sidebar.header("Manage Note")
st.title('Edit Note')
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

info = st.text_input('Note info', 'content: Life of Brian')

if st.button('Save note'):
    # st.write('Why hello there')
    note_id = slugid.nice()
    notes = for_notes('default')
    paras = {'note_id': note_id,
             'note_name': title,
             'note_info': info}
    response = notes.create_note_with_args(**paras)
    st.write("create note: ",
          note_id,
          response.result,
          response.message)
else:
    st.write('Goodbye')

# note_panel()

search_id = st.text_input('Search by note-id', '')
if st.button('Search note'):
    if search_id=='':
        st.error("Must input note-id")
    else:
        note = for_notes('default').get_note(search_id)
        note_json=json_format.MessageToJson(note)
        st.json(note_json)

