import streamlit as st
from PIL import Image

st.header('Interior Design')

img = st.file_uploader('Upload Image')
img1 = Image.open(img)
img1 = img1.convert("L")

col1,col2 = st.columns(2)
cont1 = col1.container(border=True)
cont1.write('Original Image')
cont1.image(img)

cont2 = col2.container(border=True)
cont2.write('Grayscale Image')
cont2.image(img1)
