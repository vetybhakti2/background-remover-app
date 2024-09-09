import streamlit as st
from PIL import Image
from rembg import remove
import io

# Layout with two columns
col1, col2 = st.columns([1, 5])  # Adjust the ratio as needed
with col1:
    # Display an image on the left
    logo = Image.open("/Users/vetybhakti/Documents/Vety/background-remover-app/assets/image.png")  # Replace with the path to your logo or image
    st.image(logo, width=100)  # Adjust the width as needed

with col2:
    # Application title on the right
    st.title("Background Remover App")
    st.write("by Vety Bhakti Lestari")

# Application description
st.write("-------------------------------------------------------------")
st.write("Upload images to remove their backgrounds and get the results.")

# File upload for multiple files
uploaded_files = st.file_uploader("Choose images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files is not None:
    for uploaded_file in uploaded_files:
        # Read the uploaded image
        image = Image.open(uploaded_file)

        # Display the original image
        st.image(image, caption=f"Original Image: {uploaded_file.name}", use_column_width=True)

        # Spinner to show processing
        with st.spinner(f'Removing background from {uploaded_file.name}, please wait...'):
            # Remove background
            result = remove(image)

        # Display the image with the background removed
        st.image(result, caption=f"Image Without Background: {uploaded_file.name}", use_column_width=True)

        # Button to download the resulting image
        img_byte_arr = io.BytesIO()
        result.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        st.download_button(label=f"Download {uploaded_file.name}", data=img_byte_arr, file_name=f"{uploaded_file.name.split('.')[0]}_output.png", mime="image/png")