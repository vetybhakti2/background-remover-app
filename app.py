import streamlit as st
from PIL import Image
from rembg import remove
import io

# Judul Aplikasi
st.title("Background Remover")

# Deskripsi Aplikasi
st.write("Upload gambar yang ingin dihapus background-nya dan dapatkan hasilnya.")

# File Upload
uploaded_file = st.file_uploader("Pilih gambar", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Baca gambar yang di-upload
    image = Image.open(uploaded_file)

    # Tampilkan gambar asli
    st.image(image, caption="Gambar Asli", use_column_width=True)

    # Menghapus background
    result = remove(image)

    # Menampilkan gambar yang sudah di-remove background-nya
    st.image(result, caption="Gambar Tanpa Background", use_column_width=True)

    # Tombol untuk mengunduh gambar hasil
    img_byte_arr = io.BytesIO()
    result.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    st.download_button(label="Download Gambar", data=img_byte_arr, file_name="output.png", mime="image/png")