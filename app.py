import streamlit as st

st.title('Hihi')
st.title('Here is :violet[ziyi] :sunglasses:')

col1, col2 = st.columns(2)
col1.image('image/IMG_1437.JPG', caption='in a library')

st.header('About', divider='gray')
st.text('a product designer with boundless curiosity :)')

st.subheader('Education')
st.text('B.A in information Design')
st.subheader('Work Experience')
st.text('work in Kwai-Y-tech,Conducted in-depth user research to identify the targeted users, find their usage habits and preferences, performed contrast analysis with competing products')
st.subheader('Hobbies and Interests')
st.text('photography')
