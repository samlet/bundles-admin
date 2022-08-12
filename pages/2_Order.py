import streamlit as st

st.sidebar.header("Manage Note")
st.title('Edit Note')
title = st.text_input('Movie title', 'Life of Brian')

rels = {
    'contactMech': 'Contact Mech',
    'orderRole': 'Order Role',
    'orderSlots': 'Order Slots',
}
st.sidebar.markdown("### Bundle Attachments")
selected_layers = [
    layer
    for layer_name, layer in rels.items()
    if st.sidebar.checkbox(layer, True)
]

if not selected_layers:
    st.error("Please choose at least one layer above.")
