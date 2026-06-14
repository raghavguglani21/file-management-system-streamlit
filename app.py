import streamlit as st
import pathlib
import os

# --------------------
# Page Configuration
# --------------------
st.set_page_config(
    page_title="File Management System",
    page_icon="📁",
    layout="wide"
)

# --------------------
# Custom CSS
# --------------------
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}

.hero {
    padding: 25px;
    border-radius: 15px;
    background: linear-gradient(135deg,#4F46E5,#7C3AED);
    color:white;
    text-align:center;
    margin-bottom:20px;
}

.card {
    background-color:#1E293B;
    padding:20px;
    border-radius:15px;
    box-shadow:0 4px 10px rgba(0,0,0,0.3);
}
</style>
""", unsafe_allow_html=True)

# --------------------
# Header
# --------------------
st.markdown("""
<div class="hero">
    <h1>📁 File Management System</h1>
    <p>Create, Read, Update, Rename and Delete Files Easily</p>
</div>
""", unsafe_allow_html=True)

# --------------------
# Sidebar
# --------------------
menu = st.sidebar.radio(
    "Navigation",
    [
        "Create File",
        "Read File",
        "Append Content",
        "Overwrite File",
        "Rename File",
        "Delete File"
    ]
)

# --------------------
# Create File
# --------------------
if menu == "Create File":

    st.subheader("📄 Create New File")

    filename = st.text_input("File Name")
    content = st.text_area("Content")

    if st.button("Create File"):

        path = pathlib.Path(filename)

        if path.exists():
            st.error("File already exists.")
        else:
            with open(filename, "w") as f:
                f.write(content)

            st.success("File created successfully!")

# --------------------
# Read File
# --------------------
elif menu == "Read File":

    st.subheader("📖 Read File")

    filename = st.text_input("Enter File Name")

    if st.button("Read"):

        path = pathlib.Path(filename)

        if path.exists():

            with open(filename, "r") as f:
                data = f.read()

            st.text_area(
                "File Content",
                value=data,
                height=300
            )

        else:
            st.error("File does not exist.")

# --------------------
# Append Content
# --------------------
elif menu == "Append Content":

    st.subheader("➕ Append Content")

    filename = st.text_input("File Name")
    content = st.text_area("Content to Append")

    if st.button("Append"):

        path = pathlib.Path(filename)

        if path.exists():

            with open(filename, "a") as f:
                f.write(content)

            st.success("Content appended successfully!")

        else:
            st.error("File does not exist.")

# --------------------
# Overwrite File
# --------------------
elif menu == "Overwrite File":

    st.subheader("✏️ Overwrite File")

    filename = st.text_input("File Name")
    content = st.text_area("New Content")

    if st.button("Overwrite"):

        path = pathlib.Path(filename)

        if path.exists():

            with open(filename, "w") as f:
                f.write(content)

            st.success("File overwritten successfully!")

        else:
            st.error("File does not exist.")

# --------------------
# Rename File
# --------------------
elif menu == "Rename File":

    st.subheader("🔄 Rename File")

    old_name = st.text_input("Current File Name")
    new_name = st.text_input("New File Name")

    if st.button("Rename"):

        path = pathlib.Path(old_name)

        if path.exists():

            os.rename(old_name, new_name)

            st.success(
                f"Renamed '{old_name}' to '{new_name}'"
            )

        else:
            st.error("File does not exist.")

# --------------------
# Delete File
# --------------------
elif menu == "Delete File":

    st.subheader("🗑 Delete File")

    filename = st.text_input("File Name")

    if st.button("Delete"):

        path = pathlib.Path(filename)

        if path.exists():

            os.remove(filename)

            st.success("File deleted successfully!")

        else:
            st.error("File does not exist.")

# --------------------
# Footer
# --------------------
st.sidebar.markdown("---")
st.sidebar.info(
    "Built with Python & Streamlit 🚀"
)
