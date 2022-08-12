from io import StringIO

import streamlit as st
from datetime import time, datetime, date

st.sidebar.header("Dev Stuffs")
st.title('Dev Stuffs')
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

with st.expander("See explanation"):
    st.write("""
         The chart above shows some numbers I picked for you.
         I rolled actual dice for these, so they're *guaranteed* to
         be random.
     """)
    st.image("https://static.streamlit.io/examples/dice.jpg")

agree = st.checkbox('I agree')
if agree:
    st.write('Great!')

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)

# sliders ----------
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# And here's an example of a range slider:

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# This is a range time slider:

appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Finally, a datetime slider:

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

# -------------

number = st.number_input('Insert a number')
st.write('The current number is ', number)

txt = st.text_area('Text to analyze', '''
     It was the best of times, it was the worst of times, it was
     the age of wisdom, it was the age of foolishness, it was
     the epoch of belief, it was the epoch of incredulity, it
     was the season of Light, it was the season of Darkness, it
     was the spring of hope, it was the winter of despair, (...)
     ''')
# st.write('Sentiment:', run_sentiment_analysis(txt))

# date-time
d = st.date_input(
    "When's your birthday",
    date(2019, 7, 6))
st.write('Your birthday is:', d)

t = st.time_input('Set an alarm for', time(8, 45))
st.write('Alarm is set for', t)

# radio
genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")

# -------- file uploader
# uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
#      # To read file as bytes:
#      bytes_data = uploaded_file.getvalue()
#      st.write(bytes_data)
#
#      # To convert to a string based IO:
#      stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
#      st.write(stringio)
#
#      # To read file as string:
#      string_data = stringio.read()
#      st.write(string_data)
#
#      # Can be used wherever a "file-like" object is accepted:
#      dataframe = pd.read_csv(uploaded_file)
#      st.write(dataframe)

# Insert a file uploader that accepts multiple files at a time:
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

# columns
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

# The delta indicator color can also be inverted or turned off:
st.metric(label="Gas price", value=4, delta=-0.5,
          delta_color="inverse")

st.metric(label="Active developers", value=123, delta=123,
          delta_color="off")

## download
text_contents = '''This is some text'''
st.download_button('Download some text', text_contents)

